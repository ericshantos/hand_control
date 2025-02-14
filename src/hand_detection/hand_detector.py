# -*- coding: utf-8 -*-
"""
@Author: Eric dos Santos (ericshantos13@gmail.com)
Module for hand detection and tracking with MediaPipe, processing joint coordinates in images.
"""

import cv2
import mediapipe as mp
from typing import List, Tuple
import numpy as np

class HandDetector:
    """
    Class for detecting and tracking hands using the MediaPipe framework
    """

    def __init__(self, 
        max_hands: int = 2, 
        conf_detec: float = 0.5, 
        conf_tracking: float = 0.5, 
        drawing: bool = True
        ):
        """
        Initialize the hands detector

        :param max_hands: Maximum number of hands to be detected.
        :param conf_detec: Minimum confidence required for detection.
        :param conf_tracking:  Minimum confidence required for tracking. 
        :param drawing: If true, drawing the landmarks in the image.
        """
        self.max_hands = max_hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=conf_detec, 
            min_tracking_confidence=conf_tracking
        )
        self.mp_drawing = mp.solutions.drawing_utils
        self.drawing = drawing

    def found_hands(self, image: np.ndarray) -> np.ndarray:
        """
        Process the image for hand detection.

        :param image: Input image (numpy array).
        :return: Processed image ou None if nothing was detected.
        """
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) if image.shape[-1] != 3 else image
        self.results = self.hands.process(imageRGB)

        if self.results.multi_hand_landmarks:
            hands_to_process = self.results.multi_hand_landmarks[:self.max_hands]
            for hands_pnt_ref in hands_to_process:
                if self.drawing:
                    self.mp_drawing.draw_landmarks(image, hands_pnt_ref, self.mp_hands.HAND_CONNECTIONS)

        return image


    def found_position(self, image: np.ndarray, num_hands: int = 0) -> List[Tuple[int, int, int]]:
        """
        Get the landmark positions of a blocked hand in the image.

        :param image: Input image (numpy Array).
        :param num_hands: Hand index in the detected list.
        :return: List of landmarks coordinates ou None if no hand is detected.
        """
        list_pnt_ref = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[num_hands]
            height, width, _ = image.shape

            for id, pnt_ref in enumerate(my_hand.landmark):
                px, py = int(pnt_ref.x * width), int(pnt_ref.y * height)
                list_pnt_ref.append((id, px, py))
                if self.drawing:
                    cv2.circle(image, (px, py), 15, (0, 255, 0), cv2.FILLED)
        return list_pnt_ref
