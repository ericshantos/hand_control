# -*- coding: utf-8 -*-
"""
Package for calculate Euclidean distance between thumb and index fingertips.

This package contains the `DistanceCalculator` class, which provides methods for calculating
distances between specific hand landmarks. Currently, there is one method to calculate
the distance between the thumb and index fingertip using the coordinates of the landmarks.

Classes:
    DistanceCalculator: Class responsible for calculating distances between landmarks.
"""

from .distance_calculator import DistanceCalculator

__all__ = ["DistanceCalculator"]

# Author
__author__ = "Eric dos Santos <github.com/ericSantos/hand_control>"
