SwiftSerialize
==============

*Copyright (c) 2025 Sean Yeatts. All rights reserved.*

A simple way to read and write structured data. Easily extendable to support custom data formats.


Key Features
------------
- Easily read, write, and convert between structured data formats ( ex. json, yaml ).
- Provides convenience methods for de-nesting / re-nesting hierarchical datasets.
- Encode to binary for middleman services ( ex. encryption ).


Quickstart
----------

**Example** - conversion between two structured data formats :

.. code:: python

  # IMPORTS
  from swiftserialize import JSONSerializer, YAMLSerializer


  # MAIN DEFINITION
  def main() -> None:

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
      main()


**Example** - introducing a middleman service :

.. code:: python

  # IMPORTS
  from swiftserialize import YAMLSerializer


  # MOCKUP FUNCTIONS
  def encrypt(data: bytes) -> bytes:
      """Placeholder mock encryption service."""
      return data


  # MAIN DEFINITION
  def main() -> None:

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
      main()


**Example** - manipulating nested datasets :

.. code:: python

  # IMPORTS
  from swiftserialize import YAMLSerializer


  # MAIN DEFINITION
  def main() -> None:

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
      main()


Installation
------------
**Prerequisites:**

- Python 3.8 or higher is recommended
- pip 24.0 or higher is recommended

**For a pip installation:**

Open a new Command Prompt. Run the following command:

.. code:: sh

  py -m pip install swiftserialize

**For a local installation:**

Extract the contents of this module to a safe location. Open a new terminal and navigate to the top level directory of your project. Run the following command:

.. code:: sh

  py -m pip install "DIRECTORY_HERE\swiftserialize\dist\swiftserialize-1.0.0.tar.gz"

- ``DIRECTORY_HERE`` should be replaced with the complete filepath to the folder where you saved the SwiftSerialize module contents.
- Depending on the release of SwiftSerialize you've chosen, you may have to change ``1.0.0`` to reflect your specific version.
