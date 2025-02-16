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
    Class for processing hand landmarks, including detecting hand positions,
    differentiating between left and right hands, and drawing landmarks on the image.

    Inherits from InitializeDetector class to initialize the hand detection model.

    Attributes:
        mp_drawing: Mediapipe drawing utilities for drawing landmarks.
        drawing: Boolean flag to indicate whether landmarks should be drawn on the image.
    """

    def __init__(
        self,
        max_hands: int = 2,
        conf_detec: float = 0.5,
        conf_tracking: float = 0.5,
        drawing: bool = True,
    ):
        """
        Initialize the hand landmark processor with given configurations.

        :param max_hands: Maximum number of hands to detect. Default is 2.
        :param conf_detec: Confidence threshold for hand detection. Default is 0.5.
        :param conf_tracking: Confidence threshold for hand tracking. Default is 0.5.
        :param drawing: If True, draw the landmarks on the image. Default is True.
        """
        super().__init__(max_hands, conf_detec, conf_tracking)
        self.mp_drawing = mp.solutions.drawing_utils
        self.drawing = drawing

    def detect_hands(self, image: np.ndarray) -> np.ndarray:
        """
        Detect hands in the input image, differentiate between left and right hands,
        and optionally draw landmarks on the image.

        :param image: Input image in which hands will be detected.
        :return: Image with drawn hand landmarks and hand labels.
        """
        self.process_image(image)

        if self.results and self.results.multi_hand_landmarks:
            for hands_pnt_ref in self.results.multi_hand_landmarks:
                if self.drawing:
                    # Draws the hand landmarks and connections on the image.
                    self.mp_drawing.draw_landmarks(
                        image, hands_pnt_ref, self.mp_hands.HAND_CONNECTIONS
                    )

        return image

    def get_hand_landmarks(
        self, image: np.ndarray, num_hands: int = 0
    ) -> Tuple[List[Tuple[int, int, int]], str]:
        """
        Get hand landmark positions and the corresponding hand label (left or right).

        :param image: Input image containing hands.
        :param num_hands: Index of the hand (default is 0 for the first detected hand).
        :return: A tuple containing a list of landmark coordinates and the hand label
                (either 'Left' or 'Right').
        """
        landmarks: List[Tuple[int, int, int]] = []
        hand_label = "Unknown"

        if self.results and self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[num_hands]
            height, width, _ = image.shape

            # Get the hand label (Left or Right).
            hand_label = (
                self.results.multi_handedness[num_hands].classification[0].label
            )

            for id, pnt_ref in enumerate(my_hand.landmark):
                px, py = int(pnt_ref.x * width), int(pnt_ref.y * height)
                landmarks.append((id, px, py))

                if self.drawing:
                    cv2.circle(image, (px, py), 15, (0, 255, 0), cv2.FILLED)

        return landmarks, hand_label
