import math

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
    divisors : int
    below = int

    Returns
    -------
    sum_of_multiples : int
        sum of multiples of the divisors that are less than the number below

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
    k , j = divisors

    multiples = [i for i in range(1, math.ceil(below)) if \
                is_multiple(i, k) or is_multiple(i, j)]
    sum_of_multiples = sum(multiples)

    return(sum_of_multiples)



if __name__ == "__main__":
    assert(sum_of_all_multiples(divisors = [3,5], below = 10) == 23)

    import doctest
    doctest.testmod()
