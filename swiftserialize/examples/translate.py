# Copyright (c) 2025 Sean Yeatts. All rights reserved.

from __future__ import annotations


# IMPORTS ( STANDARD )
import sys

# IMPORTS ( PROJECT )
from swiftserialize import JSONSerializer, YAMLSerializer


# MAIN DEFINITION
def main(args: list[str]) -> None:

    # [1] Prepare some input / output files
    file_in = "examples/data/translate/input.yaml"
    file_out = "examples/data/translate/output.json"

    # [2] Read data from input file
    with open(file_in, 'rb') as target:
        data = target.read()

    # [3] Translate between structured data formats
    decoded: dict = YAMLSerializer('utf-8').decode(data)
    encoded: bytes = JSONSerializer('utf-8').encode(decoded)

    # [4] Write data to output file
    with open(file_out, "wb") as target:
        target.write(encoded)

    # [5] Visualize results
    print(decoded)
    print(encoded)


# ENTRY POINT
if __name__ == "__main__":
    main(sys.argv[1:])
