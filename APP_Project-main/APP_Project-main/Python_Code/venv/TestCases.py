import unittest

from Cos import cos
from Sin import sin
from math import isclose

class MyTestCase(unittest.TestCase):
    def test_cos(self):
        assert cos(0) == 1, print("Passed")  # Testing cos(pi/2)

    def test_cos_1(self):
        assert isclose(cos(3.14 / 3), 0.5, abs_tol=1e-2) == True, print("Passed")  # Testing cos(pi/3)

    def test_sin(self):
        assert sin(0) == 0, print("Passed")  # Testing sin(0)

    def test_sin_1(self):
        assert isclose(sin(3.14 / 2), 1, abs_tol=1e-2) == True, print("Passed")

    # def test_circle_area(self):
    #     assert isclose(Circle.Circle.area(8),201.06192, abs_tol=1e-3) == True, print("Passed")

    # def test_circle_circumference(self):
    #     assert isclose(Circle.Circle.circumference(8),50.26548, abs_tol=1e-3) == True, print("Passed")

    # def test_newton_method(self):
    #     assert


if __name__ == '__main__':
    unittest.main()
