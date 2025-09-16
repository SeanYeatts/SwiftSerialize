# Copyright (c) 2025 Sean Yeatts. All rights reserved.

from __future__ import annotations


# IMPORTS ( STANDARD )
import json

# IMPORT ( PROJECT )
from swiftserialize import StructuredTextSerializer


# CLASSES
class JSONSerializer(StructuredTextSerializer):

    # OVERRIDDEN METHODS
    def encode(self, data: dict) -> bytes:
        """Converts a Python dictionary into a JSON byte string."""
        string = json.dumps(data, sort_keys=False)
        return string.encode(self.encoding)
    
    def decode(self, data: bytes) -> dict:
        """Converts a JSON byte string to a Python dictionary."""
        string = data.decode(self.encoding)
        return json.loads(string)
