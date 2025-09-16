# Copyright (c) 2025 Sean Yeatts. All rights reserved.

from __future__ import annotations


# IMPORTS ( STANDARD )
import sys

# IMPORTS ( PROJECT )
from swiftserialize import JSONSerializer


# MAIN DEFINITION
def main(args: list[str]) -> None:

    # [1] Prepare some complex structured (dict) data
    data = {
        "key-1": {
            "key-1A": "value-1A"
        },
        "key-2": {
            "key-2A": "value-2A",
            "key-2B": "value-2B",
            "key-2C": "value-2C"
        },
        "key-3": {
            "key-3A": "value-3A",
            "key-3B": "value-3B",
        },
    }

    # [2] Encode using an appropriate serializer
    serializer = JSONSerializer('utf-8')
    encoded = serializer.encode(data)

    # [3] Write data to output file
    with open("examples/data/write/output.json", "wb") as target:
        target.write(encoded)


# ENTRY POINT
if __name__ == "__main__":
    main(sys.argv[1:])
