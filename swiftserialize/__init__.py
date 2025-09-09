"""
SwiftSerialize
==============

Copyright (c) 2025 Sean Yeatts. All rights reserved.

A simple way to read and write structured data. Easily extendable to support custom data formats.
"""

from __future__ import annotations

__title__       = "swiftserialize"
__author__      = "Sean Yeatts"
__copyright__   = "Copyright (c) 2025 Sean Yeatts. All rights reserved."


# IMPORTS ( STANDARD )
import logging

# IMPORTS ( PROJECT )
from .swiftserialize import *
from .classes import (
    CSVSerializer,
    JSONSerializer,
    YAMLSerializer
)

# NULL LOGGER INITIALIZATION
logging.getLogger(__name__).addHandler(logging.NullHandler())
