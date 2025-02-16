# -*- coding: utf-8 -*-
"""
@Author: Eric dos Santos (ericshantos13@gmail.com)
Module for calculating distances between hand frames.
"""

import math
from typing import List, Tuple


class DistanceCalculator:
    """
    Class for calculating distances between hand landmarks.
    """

    @staticmethod
    def thumb_index_distance(landmarks: List[Tuple[int, int, int]]) -> int:
        """
        Calculate Euclidean distance between thumb and index fingertips.

        :param landmarks: List of landmark positions.
        :return: Distance between thumb (id 4) and index finger (id 8).
        """
        if landmarks:
            try:
                thumb_tip = next((x, y) for id, x, y in landmarks if id == 4)
                index_tip = next((x, y) for id, x, y in landmarks if id == 8)

                return int(
                    math.sqrt(
                        (index_tip[0] - thumb_tip[0]) ** 2
                        + (index_tip[1] - thumb_tip[1]) ** 2
                    )
                )
            except StopIteration:
                return 0
        return 0
