*Copyright (c) 2025 Sean Yeatts, Inc. All rights reserved.*

SwiftSerialize
==============

A simple way to read and write structured data. Easily extendable to support custom data formats.

Key Features
------------
- Easily read, write, and convert between structured data formats ( ex. json, yaml ).
- Provides convenience methods for de-nesting / re-nesting hierarchical datasets.
- Encode to binary for middleman services ( ex. data encryption ).


Quickstart
----------

Key ``import`` statements :

.. code:: python

  from swiftserialize import JSONSerializer, YAMLSerializer

**Example** - convert between two structured data formats :

.. code:: python

  # IMPORTS
  from swiftserialize import JSONSerializer, YAMLSerializer


  # MOCKUP FUNCTIONS
  def encrypt(data: bytes) -> bytes:
      """Placeholder encryption service."""
      return data


  # MAIN DEFINITION
  def main() -> None:

      # [1] Prepare some files
      file_1 = fr"cache\test.yaml"
      file_2 = fr"cache\test.json"

      # [2] Load structured data directly into a Python dict
      data: dict = YAMLSerializer().load(file_1)

      # [3] Write directly to a different structured format
      JSONSerializer().save(data, file_2)


  # ENTRY POINT
  if __name__ == "__main__":
      main()
