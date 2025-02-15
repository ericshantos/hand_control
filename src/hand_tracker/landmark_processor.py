"""
@Author: Eric dos Santos (ericshantos13@gmail.com)
Module for detection and processing of hand landmarks.
"""

from typing import List, Tuple

import cv2
import mediapipe as mp
import numpy as np

from . import InitializeDetector


class HandLandmarkProcessor(InitializeDetector):
    """
    Class for processing hand landmarks.
    """

    def __init__(
        self,
        max_hands: int = 2,
        conf_detec: float = 0.5,
        conf_tracking: float = 0.5,
        drawing: bool = True,
    ):
        """
        Initialize the hand landmark processor.

        :param drawing: If True, draw the landmarks on the image.
        """
        super().__init__(max_hands, conf_detec, conf_tracking)
        self.mp_drawing = mp.solutions.drawing_utils
        self.drawing = drawing

    def detect_hands(self, image: np.ndarray) -> np.ndarray:
        """
        Detect hands and optionally draw landmarks.

        :param image: Input image.
        :return: Image with drawn landmarks.
        """
        self.process_image(image)

        if self.results and self.results.multi_hand_landmarks:
            for hands_pnt_ref in self.results.multi_hand_landmarks[: self.max_hands]:
                if self.drawing:
                    self.mp_drawing.draw_landmarks(
                        image, hands_pnt_ref, self.mp_hands.HAND_CONNECTIONS
                    )

        return image

    def get_hand_landmarks(
        self, image: np.ndarray, num_hands: int = 0
    ) -> List[Tuple[int, int, int]]:
        """
        Get hand landmark positions.

        :param image: Input image.
        :param num_hands: Index of the hand.
        :return: List of landmark coordinates.
        """
        landmarks: List[Tuple[int, int, int]] = []
        if self.results and self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[num_hands]
            height, width, _ = image.shape

            for id, pnt_ref in enumerate(my_hand.landmark):
                px, py = int(pnt_ref.x * width), int(pnt_ref.y * height)
                landmarks.append((id, px, py))
                if self.drawing:
                    cv2.circle(image, (px, py), 15, (0, 255, 0), cv2.FILLED)
        return landmarks
