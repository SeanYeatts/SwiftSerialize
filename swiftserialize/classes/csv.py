# Copyright (c) 2025 Sean Yeatts. All rights reserved.

from __future__ import annotations


# IMPORTS ( STANDARD )
import csv
from io import StringIO

# IMPORT ( PROJECT )
from swiftserialize import TabularTextSerializer


# CLASSES
class CSVSerializer(TabularTextSerializer):

    # OVERRIDDEN METHODS
    def encode(self, data: list[dict]) -> bytes:
        """Converts a Python list ( rows ) of dicts ( columns ) into a CSV byte string."""
        buffer = StringIO()
        fieldnames = data[0].keys()
        writer = csv.DictWriter(buffer, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
        string = buffer.getvalue()
        return string.encode(self.encoding)

    def decode(self, data: bytes) -> list[dict]:
        """Converts a CSV byte string into a Python list ( rows ) of dicts ( columns )."""
        decoded = data.decode(self.encoding)
        buffer = StringIO(decoded)
        reader = csv.DictReader(buffer)
        return [dict(row) for row in reader]
