"""
@Author: Eric dos Santos (ericshantos13@gmail.com)
Module for initializing hand detection using MediaPipe.
"""

import cv2
import mediapipe as mp
import numpy as np


class InitializeDetector:
    """
    Base class for hand detection using MediaPipe.
    """

    def __init__(
        self, max_hands: int = 2, conf_detec: float = 0.5, conf_tracking: float = 0.5
    ):
        """
        Initialize the hand detector with MediaPipe.

        :param max_hands: Maximum number of hands to detect.
        :param conf_detec: Confidence threshold for detection.
        :param conf_tracking: Confidence threshold for tracking.
        """
        self.max_hands = max_hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=conf_detec, min_tracking_confidence=conf_tracking
        )
        self.results = None

    def process_image(self, image: np.ndarray):
        """
        Convert image to RGB and process it with MediaPipe.

        :param image: Input image (numpy array).
        """
        imageRGB = (
            cv2.cvtColor(image, cv2.COLOR_BGR2RGB) if image.shape[-1] != 3 else image
        )
        self.results = self.hands.process(imageRGB)
