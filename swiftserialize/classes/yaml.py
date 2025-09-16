# Copyright (c) 2025 Sean Yeatts. All rights reserved.

from __future__ import annotations


# IMPORTS ( EXTERNAL )
import yaml

# IMPORT ( PROJECT )
from swiftserialize import StructuredTextSerializer


# CLASSES
class YAMLSerializer(StructuredTextSerializer):
    
    # OVERRIDDEN METHODS
    def encode(self, data: dict) -> bytes:
        """Converts a Python dictionary into a YAML byte string."""
        string = yaml.safe_dump(data, sort_keys=False, allow_unicode=True)
        return string.encode(self.encoding)
    
    def decode(self, data: bytes) -> dict:
        """Converts a YAML byte string to a Python dictionary."""
        string = data.decode(self.encoding)
        return yaml.safe_load(string)
