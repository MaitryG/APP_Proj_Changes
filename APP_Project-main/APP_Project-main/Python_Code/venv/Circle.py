from PI import PI


class Circle:

    def __init__(self, radius):
        """
            Initializes a Circle object with the given radius.
            Raises a ValueError if radius is negative.

            :param radius: float, the radius of the circle
            """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        """
           Calculates and returns the area of the circle.

           :return: float, the area of the circle
           """
        return PI() * self.radius ** 2

    def circumference(self):
        """
          Calculates and returns the circumference of the circle.

          :return: float, the circumference of the circle
          """
        return 2 * PI() * self.radius
