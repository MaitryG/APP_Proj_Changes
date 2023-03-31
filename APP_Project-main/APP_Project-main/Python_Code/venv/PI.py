# Using Leibniz Formula to calculate approximate value of PI,
# Leibniz formula for PI, is an infinite series that can be used to approximate the value of pi.
# π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...
# this formula uses alternating signs to converge to PI.
# Following is the python code implementation of Leibniz Formula
# number of terms used for approximation


def PI():
    """
    Estimate the value of pi using the Leibniz formula and return the calculated value.

    The Leibniz formula is a way to estimate pi based on an alternating series. The more terms
    of the series that are added together, the more accurate the estimate becomes.

    Returns:
    --------
    float: The estimated value of pi.

    Raises:
    -------
    Exception: If an error occurs during calculation.

    Example:
    --------
    >>> PI()
    3.1415916535897743
    """

    try:
        number_of_terms = 1000000

        result = 0
        sign = 1

        for i in range(number_of_terms):
            new_term = sign / (2 * i + 1)
            result = result + new_term
            sign *= -1

        # use this sum to estimate PI

        pi = 4 * result
        return pi

    except Exception as e:
        print('Error:', e)