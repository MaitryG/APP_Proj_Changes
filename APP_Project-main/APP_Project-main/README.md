# APP_Project

Algorithms Used ----

Using Leibniz Formula to calculate approximate value of PI,
Leibniz formula for PI, is an infinite series that can be used to approximate the value of pi.
π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...

Using Taylor series expansion to calculate the sign function
sin(x) = x - (x^3)/3! + (x^5)/5! - (x^7)/7! + ...

Using Taylor series expansion to calculate the Cosine function
cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + ...

Newton method in Python to solve for alpha given the equation 
α – sin(α) = π/2. 

l = 2R(1 – cos(α/2))    // Using the values of α calculated using the Newton Method


# Different methods for calculating Pi

1. Monte Carlo method: This involves generating random points inside a square and counting the number of points that fall inside a circle inscribed in the square. The ratio of the number of points inside the circle to the total number of points can be used to estimate the value of pi.

2. Leibniz formula: This involves using the series expansion of arctan(x) to approximate pi/4. The formula is pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ... . The more terms in the series, the better the approximation.

# Why Choose Leibniz ?

Depending on the application and amount of precision required, Monte Carlo or the Leibniz formula may be preferable for estimating pi.
When a very large number of decimal places of pi are required, the Monte Carlo approach may be more effective since it may attain great precision with very few calculations. Nevertheless, it can be computationally demanding and need the generation of several random numbers, which can take a lot of time. For estimating pi, the Leibniz formula is a reasonably easy-to-understand formula that may be quickly calculated for a given number of terms.

References :

https://www.geeksforgeeks.org/calculate-pi-with-python/

https://iq.opengenus.org/different-ways-to-calculate-pi/


# These are several ways to compute the sin(x) function in Python without using any libraries

1. Using the Taylor series expansion: One way to compute the sin(x) function is to use the Taylor series expansion. The Taylor series expansion for sin(x) is:

sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
We can compute sin(x) by summing up the first n terms of this series, where n is some positive integer.

2. Using the CORDIC algorithm: The CORDIC (COordinate Rotation DIgital Computer) algorithm is a method for computing trigonometric functions that uses only simple shift, add, and subtract operations. The algorithm iteratively rotates a vector by a series of fixed angles to compute the sine and cosine of an angle. The number of iterations determines the accuracy of the result.

3. Using the Chebyshev polynomial approximation: The Chebyshev polynomial approximation is a method for computing trigonometric functions that uses a series of Chebyshev polynomials to approximate the function. The method is more accurate than the Taylor series expansion and can be computed efficiently using a recursive formula.


# Why Taylor Series ?

When a high level of precision is required and the function can be reasonably approximated by a polynomial, Taylor series are a solid option. They perform best when the function is bounded and highly differentiable. For elementary computations, the Taylor series expansion for sine and cosine is a useful option since it is comparatively easy to understand.
