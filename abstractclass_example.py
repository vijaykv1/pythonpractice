import sys
import abc


class Animal(abc.ABC):
    """Animal Class for representing all Animals"""

    @property
    @abc.abstractmethod
    def name(self):
        """Property called Name to be present in all classes inheriting this."""
        pass

    @abc.abstractmethod
    def feed(self):
        """feed method for animals"""
        pass


class Panda(Animal):
    """Class to represent a Panda"""

    def __init__(self):
        """Constructor"""
        self.__name = None

    def feed(self):
        """Panda feed method"""
        print("I eat bamboo!!!")

    @property
    def name(self):
        """Name of animal - override"""
        return self.__name

    @name.setter
    def name(self, n):
        """Setter for animal name"""
        self.__name = n


class Snake(Animal):
    """Class to represent a Snake"""

    def __init__(self):
        """Constructor"""
        self.__name = None

    @property
    def name(self):
        """Name of current animal"""
        return self.__name

    @name.setter
    def name(self, n):
        """Setter for animal name"""
        self.__name = n

    def feed(self):
        print("I am eating Frog")


class Lion(Animal):

    def __init__(self):
        self.__n = None

    def feed(self):
        print("I eat flesh")

    @property
    def name(self):
        return self.__n

    @name.setter
    def name(self, n):
        self.__n = n


if __name__ == '__main__':

    # create a snake
    s = Snake()
    s.name = "Snake"
    print(f"Animal name {s.name}")
    s.feed()

    # create a panda
    p = Panda()
    p.name = "Panda"
    print(f"Animal name {p.name}")
    p.feed()

    sys.exit(0)
