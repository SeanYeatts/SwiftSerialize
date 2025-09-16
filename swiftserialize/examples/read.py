# Copyright (c) 2025 Sean Yeatts. All rights reserved.

from __future__ import annotations


# IMPORTS ( STANDARD )
import sys

# IMPORTS ( PROJECT )
from swiftserialize import CSVSerializer


# MAIN DEFINITION
def main(args: list[str]) -> None:

    # [1] Read some data from an input file
    with open("examples/data/read/input.csv", "rb") as target:
        data = target.read()

    # [2] Decode using an appropriate serializer
    serializer = CSVSerializer('utf-8')
    decoded = serializer.decode(data)

    # [3] Visualize result
    for index, entry in enumerate(decoded):
        print(index, f"{entry['name']}: {entry['email']}")


# ENTRY POINT
if __name__ == "__main__":
    main(sys.argv[1:])
