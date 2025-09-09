# Copyright (c) 2025 Sean Yeatts. All rights reserved.

from __future__ import annotations


# IMPORTS ( STANDARD )
import base64
import json

# IMPORTS ( PROJECT )
from swiftserialize import StructuredSerializer


# CLASSES
class JSONSerializer(StructuredSerializer):

    # OVERRIDDEN METHODS
    def encode(self, data: dict) -> bytes:
        string  = json.dumps(data)
        encoded = string.encode(self.standard)
        stream  = base64.b64encode(encoded)
        return stream
    
    def decode(self, binary: bytes) -> dict:
        stream  = base64.b64decode(binary)
        decoded = stream.decode(self.standard)
        data    = json.loads(decoded)
        return data

    # STRUCTURED METHODS
    def load(self, file: str) -> dict:
        super().load(file)
        with open(file, 'r', encoding=self.standard) as target:
            data = json.load(target)
        return data
    
    def save(self, data: dict, file: str) -> None:
        super().save(data, file)
        with open(file, 'w') as target:
            json.dump(data, target, sort_keys=False, indent=4)
