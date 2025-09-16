# Copyright (c) 2025 Sean Yeatts. All rights reserved.

from __future__ import annotations


# IMPORTS ( STANDARD )
import pandas as pd
from io import BytesIO

# IMPORT ( PROJECT )
from swiftserialize import TabularTextSerializer


# CLASSES
class CSVSerializer(TabularTextSerializer):

    # OVERRIDDEN METHODS
    def encode(self, data: list[dict]) -> bytes:
        """Converts a Python list ( rows ) of dicts ( columns ) into a CSV byte string."""
        buffer = BytesIO()
        dataframe = pd.DataFrame(data)
        dataframe.to_csv(buffer, index=False, encoding=self.encoding)
        return buffer.getvalue()

    def decode(self, data: bytes) -> list[dict]:
        """Converts a CSV byte string into a Python list ( rows ) of dicts ( columns )."""
        buffer = BytesIO(data)
        dataframe = pd.read_csv(buffer, encoding=self.encoding)
        return dataframe.to_dict(orient='records')
