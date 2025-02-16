"""
Package for controlling system properties such as screen brightness and volume.

This package provides functionality to manage system properties including screen brightness and
system volume. It utilizes the `screen_brightness_control` library for controlling the brightness
and the `Pycaw` library for controlling the system volume.

Included modules:
- `VolumeController`: A class that interfaces with the system audio endpoint to control the volume
level.
- `BrightnessController`: A class that controls screen brightness using the `screen_brightness_control`
library.

Both controllers support defining a maximum level for normalization and ensure safe adjustments to system
properties.
"""

from .brightness import BrightnessController
from .volume import VolumeController

__all__ = ["VolumeController", "BrightnessController"]

# Author
__author__ = "Eric dos Santos <github.com/ericSantos/hand_control>"
