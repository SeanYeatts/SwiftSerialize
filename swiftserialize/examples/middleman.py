# Copyright (c) 2025 Sean Yeatts. All rights reserved.

from __future__ import annotations


# IMPORTS ( STANDARD )
import sys

# IMPORTS ( PROJECT )
from swiftserialize import YAMLSerializer


# FUNCTIONS
def encrypt(data: bytes) -> bytes:
    """Placeholder mock encryption service."""
    return data


# MAIN DEFINITION
def main(args: list[str]) -> None:

    # [1] Prepare some input / output files
    file_in = "examples/data/middleman/input.yaml"
    file_out = "examples/data/middleman/output.bin"

    # [2] Read data from input file
    with open(file_in, 'rb') as target:
        data = target.read()

    # [3] Inject middleman services ( ex: encryption )
    serializer  = YAMLSerializer('utf-8')
    decoded     = serializer.decode(data)
    encrypted   = encrypt(decoded)
    encoded     = serializer.encode(encrypted)

    # [4] Write data to output file
    with open(file_out, "wb") as target:
        target.write(encoded)


# ENTRY POINT
if __name__ == "__main__":
    main(sys.argv[1:])
