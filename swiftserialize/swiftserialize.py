# Copyright (c) 2025 Sean Yeatts. All rights reserved.

from __future__ import annotations


# IMPORTS ( STANDARD )
import logging
from abc import ABC as Abstract
from abc import abstractmethod
from typing import Generic, TypeVar, Optional


# MODULE LOGGER
log = logging.getLogger(__name__)

# TYPING
T = TypeVar('T')


class Serializer(Generic[T], Abstract):
    """Base template for serializing any data format."""
    
    # ABSTRACT METHODS
    @abstractmethod
    def encode(self, data: T) -> bytes:
        """Converts a Python object into bytes."""
        ... # extended by subclasses

    @abstractmethod
    def decode(self, data: bytes) -> T:
        """Converts bytes to a Python object."""
        ... # extended by subclasses


class TextSerializer(Serializer[T], Abstract):
    """Base template for text-based data serialization."""

    # INTRINSIC METHODS
    def __init__(self, encoding: Optional[str] = 'utf-8'):
        super().__init__()
        self.encoding = encoding
    
    # ABSTRACT METHODS
    @abstractmethod
    def encode(self, data: T) -> bytes:
        """Converts a text-based Python object into bytes."""
        return super().encode(data)
    
    @abstractmethod
    def decode(self, data: bytes) -> T:
        """Converts bytes into a text-based Python object."""
        return super().decode(data)
    

class TabularTextSerializer(TextSerializer[list[dict]]):
    """Represents text-based data structured as a list ( rows ) of dictionaries ( columns )."""
    pass


class StructuredTextSerializer(TextSerializer[dict]):
    """Represents text-based data structured as a dictionary."""
    
    # UTILITY METHODS
    def pack(self, data: dict) -> dict:
        """Reconstructs a nested dictionary from flattened key-value pairs ( recursive )."""

        folded = {}

        def insert(level, keys, value):
            if isinstance(keys, tuple):                 # if the key is a tuple...
                for key in keys[:-1]:                   # get all parent keys
                    level = level.setdefault(key, {})   # initialize an empty dict
                level[keys[-1]] = value                 # set the value of the final key
            else:
                level[keys] = value                     # ...otherwise just set the value

        for keys, value in data.items():                # for each item
            if isinstance(value, dict):                 # if the value is a dict...
                nested_dict = self.fold(value)          # step another level outward
                insert(folded, keys, nested_dict)       # insert the folded result
            else:
                insert(folded, keys, value)             # ...otherwise just insert the value

        return folded

    def unpack(self, data: dict) -> dict:
        """Deconstructs a nested dictionary into flattened key-value pairs ( recursive ). *Keys
        are represented as tuples.*"""

        flattened = {}

        def traverse(source, path=()):
            for key, value in source.items():   # for each item
                new_path = path + (key,)        # update the composite key
                if isinstance(value, dict):     # if the value is a dict...
                    traverse(value, new_path)   # step another level deeper
                else:
                    flattened[new_path] = value # ...otherwise create an entry

        traverse(data)
        return flattened
