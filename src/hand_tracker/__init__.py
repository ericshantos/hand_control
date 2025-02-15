"""
Package for hand detection and processing using MediaPipe.

This package includes classes and functions for detecting hands in images, processing hand landmarks, and calculating distances between hand landmarks. It utilizes MediaPipe for hand detection and tracking and offers additional functionality, such as drawing landmarks on images and calculating distances between fingertip points.

Included modules:
- `InitializeDetector`: Base class for hand detection with MediaPipe.
- `HandLandmarkProcessor`: Class for processing hand landmarks and drawing them on the image.
- `HandDistanceCalculator`: Class for calculating distances between hand landmarks.

Each class can be configured with custom parameters for detection, tracking, and landmark drawing.
"""

import logging

from .distance_calculator import HandDistanceCalculator
from .initialize_detector import InitializeDetector
from .landmark_processor import HandLandmarkProcessor

logging.basicConfig(level=logging.DEBUG)

__all__ = ["HandDistanceCalculator", "HandLandmarkProcessor"]

# Author
__author__ = "Eric dos Santos <github.com/ericSantos/hand_control>"
