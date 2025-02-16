"""
Package for hand detection and processing using MediaPipe.

This package includes classes and functions for detecting hands in images and processing
hand landmarks. It utilizes MediaPipe for hand detection and tracking and offers additional
functionality and such as drawing landmarks on images.

Included modules:
- `InitializeDetector`: Base class for hand detection with MediaPipe.
- `HandLandmarkProcessor`: Class for processing hand landmarks and drawing them on the image.

Each class can be configured with custom parameters for detection, tracking, and landmark drawing.
"""

from .initialize_detector import InitializeDetector
from .landmark_processor import HandLandmarkProcessor

__all__ = ["HandLandmarkProcessor"]

# Author
__author__ = "Eric dos Santos <github.com/ericSantos/hand_control>"
