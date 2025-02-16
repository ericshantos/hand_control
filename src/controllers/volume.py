# -*- coding: utf-8 -*-
"""
@Author: Eric dos Santos (ericshantos13@gmail.com)
Module for controlling system volume using the Pycaw library.
"""

from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

from .controller import Controller


class VolumeController(Controller):
    """
    VolumeController class for controlling system volume using the Pycaw library.
    """

    def __init__(self, max_level: int = 300):
        """
        Initializes the VolumeController instance by obtaining the default audio output
        device and accessing its volume control interface.

        :param max_level: The maximum volume level used for normalization (default: 300).
        """
        super().__init__(max_level)
        self._device = AudioUtilities.GetSpeakers()
        self._interface = self._device.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        self._volume = self._interface.QueryInterface(IAudioEndpointVolume)

    def set_property(self, level: float):
        """
        Sets the system volume on a scale from 0.0 to 1.0.

        :param level: Desired volume level (0.0 = mute, 1.0 = maximum).
        """
        normalized_level = (level - 1) / (self.max_level - 1)
        clamped_level = super().normalize(normalized_level, 0, 1)
        self._volume.SetMasterVolumeLevelScalar(clamped_level, None)
