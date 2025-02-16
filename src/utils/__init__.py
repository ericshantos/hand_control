# -*- coding: utf-8 -*-
"""
@Author: Eric dos Santos (ericshantos13@gmail.com)
Package for calculating distances between hand landmarks.

This module contains the `DistanceCalculator` class, which provides methods for calculating
distances between specific hand landmarks. Currently, there is one method to calculate
the distance between the thumb and index fingertip using the coordinates of the landmarks.

Classes:
    DistanceCalculator: Class responsible for calculating distances between landmarks.

Methods:
    thumb_index_distance: Calculates the Euclidean distance between the thumb and index fingertip.
"""

from .distance_calculator import DistanceCalculator

__all__ = ["DistanceCalculator"]

# Author
__author__ = "Eric dos Santos <github.com/ericSantos/hand_control>"
