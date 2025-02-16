# -*- coding: utf-8 -*-
"""
@Author: Eric dos Santos (ericshantos13@gmail.com)
Module for controlling screen brightness using the screen_brightness_control library.
"""

import screen_brightness_control as sbc

from .controller import Controller


class BrightnessController(Controller):
    """
    Controller for adjusting screen brightness using the screen_brightness_control library.
    """

    def __init__(self, max_level: int = 300, display: int = 0):
        """
        Initializes the BrightnessController instance by setting the maximum brightness
        level and the display to control.

        :param max_level: The maximum brightness level used for normalization (default: 300).
        :param display: The index of the display to control (default: 0, which is usually the primary display).
        """
        super().__init__(max_level)
        self._display = display

    def set_property(self, level: float):
        """
        Sets the screen brightness on a scale from 0 to 100.

        The input level is normalized from the range [0, max_level] to a scale of [0, 100],
        ensuring that the brightness is adjusted accordingly. The current brightness level
        is checked, and if necessary, the brightness is updated.

        :param level: Desired brightness level (0 = minimum brightness, 100 = maximum brightness).
        """
        normalized_level = (level / self.max_level) * 100
        clamped_level = super().normalize(normalized_level, 0, 100)

        current_brightness = sbc.get_brightness(display=self._display)
        if clamped_level != current_brightness:
            sbc.set_brightness(clamped_level, display=self._display)
