from Circle import Circle
from Newton_Method import shift_distance


class Coaster(Circle):
    """
    A subclass of Circle representing a coaster.

    Attributes:
    - radius (float): radius of the coaster
    - overlap_area (float): area of overlap with another coaster (initialized as None)
    - distance (float): distance needed to shift the coaster for overlap to be half the area (initialized as None)

    Methods:
    - overlap(): calculates the area of overlap with another coaster and returns the value
    - shift_distance(x0): calculates the distance needed to shift the coaster for overlap to be half the area and returns the value
    - display(): returns a string containing information about the coaster (radius, area, circumference, overlap area, distance needed to shift)
    - get_radius(): returns the radius of the coaster

    Inherits methods from Circle:
    - area(): calculates the area of the coaster and returns the value
    - circumference(): calculates the circumference of the coaster and returns the value
    """

    def __init__(self, radius):
        """
        Initializes a coaster with a given radius.

        Parameters:
        - radius (float): radius of the coaster
        """
        super().__init__(radius)
        self.overlap_area = None
        self.distance = None

    def overlap(self):
        """
        Calculates the area of overlap with another coaster and returns the value.

        Returns:
        - overlap_area (float): area of overlap with another coaster
        """
        self.overlap_area = self.area() / 2
        return self.overlap_area

    def shift_distance(self, x0):
        """
        Calculates the distance needed to shift the coaster for overlap to be half the area and returns the value.

        Parameters:
        - x0 (float): starting point for the Newton-Raphson method

        Returns:
        - distance (float): distance needed to shift the coaster for overlap to be half the area
        """
        self.distance = shift_distance(x0, self.radius)
        return self.distance

    def display(self):
        """
        Returns a string containing information about the coaster (radius, area, circumference, overlap area, distance needed to shift).

        Returns:
        - string (str): string containing information about the coaster
        """
        string = ''
        string += f'{self.radius}\t'
        string += f'{self.area()}\t'
        string += f'{self.circumference()}'
        if self.overlap_area is not None:
            string += f'\nOverlap area: {self.overlap_area}'
        if self.distance is not None:
            string += f'\nDistance needed to shift coaster for overlap to be half the area: {self.distance}'
        return string

    def get_radius(self):
        """
        Returns the radius of the coaster.

        Returns:
        - radius (float): radius of the coaster
        """
        return self.radius
