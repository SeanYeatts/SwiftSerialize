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

**Example** - convert between two structured data formats :

.. code:: python

  # IMPORTS
  from swiftserialize import JSONSerializer, YAMLSerializer


  # MAIN DEFINITION
  def main() -> None:

      # [1] Prepare some files
      file_1 = fr"cache\test.yaml"
      file_2 = fr"cache\test.json"

      # [2] Load structured data directly into a Python dict
      data: dict = YAMLSerializer().load(file_1)

      # [3] Convert to a different structured format
      JSONSerializer().save(data, file_2)


  # ENTRY POINT
  if __name__ == "__main__":
      main()


**Example** - introduce a middleman service :

.. code:: python

  # IMPORTS
  from swiftserialize import YAMLSerializer


  # MOCKUP FUNCTIONS
  def encrypt(data: bytes) -> bytes:
      """Placeholder encryption service."""
      return data


  # MAIN DEFINITION
  def main() -> None:

      # [1] Prepare some files
      file_1 = fr"cache\test.yaml"
      file_2 = fr"cache\test.bin"

      # [2] Convert to binary for middleman services ( ex. encryption )
      data        = YAMLSerializer().load(file_1)
      encoded     = YAMLSerializer().encode(data)
      encrypted   = encrypt(encoded)
      
      # [3] Serialize the modified data using the same serializer
      YAMLSerializer().serialize(encrypted, file_2)


  # ENTRY POINT
  if __name__ == "__main__":
      main()


**Example** - handle nested datasets :

.. code:: python

  # IMPORTS
  from swiftserialize import YAMLSerializer


  # MAIN DEFINITION
  def main() -> None:

      # [1] Prepare a file
      file = fr"cache\test.yaml"
      
      # [2] Nested datasets can be conveniently "unpacked" into single key-value pairs
      original:   dict = YAMLSerializer().load(file)
      unpacked:   dict = YAMLSerializer().unpack(file)

      # [3] Nesting operations can be done directly with Python dicts
      flattened:  dict = YAMLSerializer().flatten(original)
      folded:     dict = YAMLSerializer().fold(flattened)

      print(original)
      print(unpacked)
      print(flattened)
      print(folded)

      # [4] Keys for flattened datasets are represented as tuples
      value = flattened.get(('PARAMETER', 'SUB-PARAMETER'))
      print(value)


  # ENTRY POINT
  if __name__ == "__main__":
      main()
