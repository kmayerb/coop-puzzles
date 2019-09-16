import math
import numpy as np

def is_multiple(x, k):
    """
    Tests if x is a multiple of k.

    Parameters
    ----------
    x : int or float
    k : int or float

    Returns
    -------
    boolean
        True if n is a multiple of k.

    Raises
    ------
    ZeroDivisionError if k is 0 or 0.0
    TypeError if x or k are strings or None

    Examples
    --------
    >>> is_multiple(9,3)
    True
    >>> is_multiple(9,2)
    False
    """
    return x % k == 0    #  True if n is a multiple of k


def sum_of_all_multiples(divisors=[3, 5], below = 10):
    """
    Find the sum of all the multiples of k or j that are below some
    number n.

    Parameters
    ----------
    divisors : list
        list of [int, int]
    below : int or float
        integer or float that all multiples must be below in order to be summed

    Returns
    -------
    sum_of_multiples : int
        the sum of multiples of the divisors that are less than the number below

    Raises
    ------
    TypeError if below is a string or None

    Examples
    --------
    >>> sum_of_all_multiples(divisors = [3,5], below= 10)
    23
    >>> sum_of_all_multiples(divisors = [3,5], below= 1000)
    233168
    """
    # Assert enforce that divisors is a list of positive integers
    assert(isinstance(divisors, list)), "divisors must be a list"
    assert(np.all([isinstance(d, int) for d in divisors])) , "divisors must be a list of integers"
    assert(np.all([d > 0 for d in divisors])) , "divisors must be a list of positive integers"

    # New Method: That can accommodate any number of divisors
    all_multiples = []

    for d in divisors:
        all_multiples = all_multiples + [i for i in range(1, math.ceil(below)) if is_multiple(i, d)]

    sum_of_multiples = sum(list(set(all_multiples)))

    # Previous Method was rigid, requiring exactly two divisors
    # k , j = divisors
    #
    # multiples = [i for i in range(1, math.ceil(below)) if \
    #            is_multiple(i, k) or is_multiple(i, j)]
    # sum_of_multiples = sum(multiples)

    return(sum_of_multiples)



if __name__ == "__main__":
    assert(sum_of_all_multiples(divisors = [3,5], below = 10) == 23)

    import doctest
    doctest.testmod()
