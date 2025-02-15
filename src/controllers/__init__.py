"""
Package for system volume control using the Pycaw library.

This package provides functionality to manage the system volume through an interface to the default audio output device. It allows setting the volume to a normalized level within a specified range.

Included modules:
- `VolumeController`: A class that interfaces with the system audio endpoint to control the volume level.

The module supports defining a maximum volume level for normalization and ensures safe volume adjustments.
"""

import logging

from .volume import VolumeController

logging.basicConfig(level=logging.DEBUG)

__all__ = [
    "VolumeController",
]

# Author
__author__ = "Eric dos Santos <github.com/ericSantos/hand_control>"
