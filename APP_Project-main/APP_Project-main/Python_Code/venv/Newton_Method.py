# In this implementation, newton_method is a function that takes as input the function f, its derivative df,
# an initial guess x0, an error tolerance eps, and a maximum number of iterations max_iter. It uses the Newton method
# to solve for the root of the function f, starting at x0 and iteratively updating the guess using the formula x - f(
# x)/f'(x). The function stops iterating when the absolute value of f(x) is less than eps, or when the derivative f'(
# x) is zero. It returns the solution x, or None if no solution was found within the maximum number of iterations. In
# this case, the function f is defined as x - sin(x) - pi/2, and its derivative df is defined as 1 - cos(x). The
# initial guess x0 is set to pi/2, since we know that the root is close to this value. The resulting alpha value is
# printed to the console.
from Cos import cos
from PI import PI
from Sin import sin
import math


def newton_method(x0, eps=1e-6, max_iter=40):
    """
        Approximates the root of a function using Newton's method.

        Args:
            x0 (float): The initial guess for the root.
            eps (float, optional): The desired tolerance for the approximation. Defaults to 1e-6.
            max_iter (int, optional): The maximum number of iterations allowed. Defaults to 1000.

        Returns:
            float: An approximation for the root of the function.

        Raises:
            ValueError: If the derivative of the function is zero at the current guess.
        """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < eps:
            return x
        fpx = df(x)
        if fpx == 0:
            raise ValueError("Derivative is zero, cannot continue")
        x = x - fx / fpx
    return x


def f(x):
    """
       Calculates the value of the function f(x) = x - sin(x) - (PI() / 2) for a given value of x.

       Args:
           x (float): The value of x at which to evaluate the function.

       Returns:
           float: The value of the function at x.
       """
       
    pi=round(PI()/2,2)
    return x - sin(x) - pi


def df(x):
    """
       Calculates the value of the derivative of the function f(x) = x - sin(x) - (PI() / 2) for a given value of x.

       Args:
           x (float): The value of x at which to evaluate the derivative.

       Returns:
           float: The value of the derivative at x.
       """
    return 1 - cos(x)   


def shift_distance(x0, R):
    """
        Calculates the distance needed to shift a circle of radius R such that it overlaps with another circle of the same radius.

        The distance is calculated using Newton's method to find the root of the function f(x) = x - sin(x) - (PI() / 2), which represents the angle needed to shift the circle.

        Args:
            x0 (float): The initial guess for the angle needed to shift the circle.
            R (float): The radius of the circle.

        Returns:
            float: The distance needed to shift the circle such that it overlaps with another circle of the same radius, or None if the derivative of the function is zero at the current guess.

        Raises:
            ValueError: If the derivative of the function is zero at the current guess (raised by the newton_method function).
        """
    try:
        alpha = newton_method(x0)
        print("alpha",alpha)
        l = 2 * R * (1 - cos(alpha / 2))
        return l / 2
    except ValueError as e:
        print(e)
        return None
