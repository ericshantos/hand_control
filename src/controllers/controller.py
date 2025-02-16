from abc import ABC, abstractmethod


class Controller(ABC):
    """
    Abstract base class that represents a controller with normalization functionality.
    """

    def __init__(self, max_level: int = 300):
        """
        Initializes the controller with a specified maximum level.
        """
        self.max_level = max_level

    def normalize(self, level: float, min_level: float, max_level: float):
        """
        Normalizes a level to be within the specified range.
        """
        return max(min_level, min(max_level, level))

    @abstractmethod
    def set_property(self, level: float):
        """
        Abstract method that must be implemented in subclasses.
        """
        pass
