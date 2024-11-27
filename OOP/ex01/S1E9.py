from abc import ABC, abstractmethod
class Character(ABC):
    """
    Class representing a Stark, inheriting from the Character class.
    """
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Constructor for the Stark class.
        Parameters:
            first_name (str): The first name of the Stark.
            is_alive (bool): The health state of the Stark, default is True.
        """
        self.first_name = first_name
        self.is_alive = is_alive


    def die(self):
        self.is_alive = False


class Stark(Character):
    """
    Constructor for the Stark class.
    Parameters:
        first_name (str): The first name of the Stark.
        is_alive (bool): The health state of the Stark, default is True.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Constructor for the Stark class.
        Parameters:
            first_name (str): The first name of the Stark.
            is_alive (bool): The health state of the Stark, default is True.
        """
        super().__init__(first_name, is_alive)
