# Copyright (c) 2025 Sean Yeatts. All rights reserved.

from __future__ import annotations


# IMPORTS ( STANDARD )
import logging
from abc import ABC as Abstract
from abc import abstractmethod
from typing import TypeVar, Generic


# MODULE LOGGER
log = logging.getLogger(__name__)

# TYPING
T = TypeVar("T")


# CLASSES
class Serializer(Abstract, Generic[T]):
    """Base interface for serializing any dataset."""

    # I/O METHODS
    def serialize(self, data: T, file: str) -> None:
        """Saves the dataset as binary to a file."""
        log.debug(f"writing data to file: '{file}'")
        stream = self.encode(data)
        with open(file, 'wb') as target:
            target.write(stream)

    def deserialize(self, file: str) -> T:
        """Loads the dataset as binary from a file."""
        log.debug(f"reading data from file: '{file}'")
        with open(file, 'rb') as target:
            stream = target.read()
        return self.decode(stream)

    # TRANSLATION METHODS
    @abstractmethod
    def encode(self, data: T) -> bytes:
        """Defines how the dataset is translated to binary."""
        ... # extended by subclasses

    @abstractmethod
    def decode(self, binary: bytes) -> T:
        """Defines how the dataset is translated from binary."""
        ... # extended by subclasses


class BinarySerializer(Serializer[bytes]):
    """Extendable interface for serializing binary datsets."""
    
    # NOTE: Explicity encoding / decoding is not necessary for binary datasets.

    # OVERRIDDEN METHODS
    def encode(self, data: bytes):
        return data

    def decode(self, binary: bytes):
        return binary


class StructuredSerializer(Serializer[dict]):
    """Extendable interface for serializing structured datasets."""

    # INTRINSIC METHODS
    def __init__(self, encoding: str = 'utf-8'):
        super().__init__()
        self.standard = encoding

    # OVERRIDDEN METHODS
    def encode(self, data: dict):
        """Translates a Python dict into structured binary."""
        return super().encode(data)
    
    def decode(self, binary: bytes):
        """Translates structured binary into a Python dict."""
        return super().decode(binary)

    # STRUCTURED METHODS
    @abstractmethod
    def save(self, data: dict, file: str) -> None:
        """Saves structured data to a file."""
        log.debug(f"saving data to file: '{file}'")
        ... # extended by subclasses

    @abstractmethod
    def load(self, file: str) -> dict:
        """Loads structured data from a file."""
        log.debug(f"loading data from file: '{file}'")
        ... # extended by subclasses

    # HELPER METHODS
    def flatten(self, data: dict) -> dict:
        """Deconstructs nested data into single key-value pairs."""
        
        result = {}

        def traverse(source, old_key=[]) -> dict:
            """Recursively traverses nested structures."""
            for key, value in source.items():           # for each item
                new_key = old_key + [key]               # update current key path
                if isinstance(value, dict):             # if we're still seeing a dictionary...
                    nesting = traverse(value, new_key)  # go one deeper
                    result.update(nesting)              # when we get back out, overwrite entry
                else:
                    result[tuple(new_key)] = value      # ...otherwise create entry
            return result
        
        return traverse(data)
    
    def fold(self, data: dict) -> dict:
        """Reconstructs nested data from single key-value pairs."""
        
        result = {}
    
        def insert(level, keys, value):
            """Injects a value into a nested dictionary structure."""
            if isinstance(keys, tuple):                 # if the key is a tuple...
                for key in keys[:-1]:                   # get all parent keys
                    level = level.setdefault(key, {})   # initialize a dict
                level[keys[-1]] = value                 # set the value of the final key
            else:
                level[keys] = value                     # ...otherwise set value directly

        for keys, value in data.items():                # for every entry in our dataset
            if isinstance(value, dict):                 # if the value is a dictionary...
                nested_dict = self.fold(value)          # recursively fold
                insert(result, keys, nested_dict)       # insert folded result
            else:
                insert(result, keys, value)             # ...otherwise insert value directly

        return result

    def pack(self, data: dict, file: str) -> None:
        """Folds and saves structured data to a file."""
        folded = self.fold(data)
        self.save(folded, file)

    def unpack(self, file: str) -> dict:
        """Loads and flattens structured data from a file."""
        data = self.load(file)
        return self.flatten(data)
