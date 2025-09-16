# Copyright (c) 2025 Sean Yeatts. All rights reserved.

from __future__ import annotations


# IMPORTS ( STANDARD )
import sys

# IMPORTS ( PROJECT )
from swiftserialize import YAMLSerializer


# MAIN DEFINITION
def main(args: list[str]) -> None:

    # [1] Read some data from an input file
    with open("examples/data/nesting/test.yaml", "rb") as target:
        data = target.read()

    # [2] Conveniently unpack / pack nested datasets
    serializer  = YAMLSerializer('utf-8')
    original    = serializer.decode(data)
    unpacked    = serializer.unpack(original)
    packed      = serializer.pack(unpacked)

    # [3] Visualize result
    print(original)
    print(unpacked)
    print(packed)

    # [4] Keys for flattened datasets are represented as tuples
    value = unpacked.get(('KEY-2', 'KEY-2A'))
    print(value)


# ENTRY POINT
if __name__ == "__main__":
    main(sys.argv[1:])
