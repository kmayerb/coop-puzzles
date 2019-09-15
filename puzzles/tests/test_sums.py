import pytest

from puzzles.sums import is_multiple
from puzzles.sums import sum_of_all_multiples

testspace = [
# null input
(3, 5, None, None, TypeError),
# strings
(3, 5, "1",  None, TypeError),
(3, 5, "A",  None, TypeError),
# negative integers
(3, 5, -10, 0, None),
(3, 5, -3, 0,  None),
# zero
(3, 5, 0, 0, None),
# the negative integers
(3, 5, -1, 0,   None),
(3, 5, -3, 0,   None),
(3, 5, -6, 0,   None),
# the positive integers
(3, 5, 1, 0,   None),
(3, 5, 2, 0,   None),
(3, 5, 3, 0,   None),
(3, 5, 4, 3,   None),
(3, 5, 6, 8,   None),
(3, 5, 7, 14,  None),
(3, 5, 10, 23, None),
(3, 5, 11, 33, None),
(3, 5, 13, 45, None),
(3, 5, 16, 60, None), # (!!! This is a really important test because 15 is a multiple of both 3 and 5).
# floats which can be interpreted as ints
(3, 5, -10.0, 0,  None),
(3, 5, -3.0,  0,  None),
(3, 5,  0.0,  0,  None),
(3, 5,  3.0,  0,  None),
(3, 5,  10.0, 23, None),
# floats not equivalent to ints - not a natural number (maybe want to raise a custom exception)
(3, 5, -10.5, 0,  None),
(3, 5, -3.5,  0,  None),
(3, 5, 0.5,   0,  None),
(3, 5, 3.5,   3,  None),
(3, 5, 10.5,  33, None)]

@pytest.mark.parametrize("x, y, z, expectation, expected_error", testspace)
def test_sum_of_all_multiples(x, y, z, expectation, expected_error):
    try:
        r = sum_of_all_multiples(divisors=[x, y], below = z)
        assert(r == expectation)
    except:
        with pytest.raises(expected_error):
            r = sum_of_all_multiples(divisors=[x, y], below = z)


testdata = [
    # Consider Representative of a Test Space
    # Natural Numbers as Floats
    (1.0,  1.0, True,  None),
    (2.0,  1.0, True,  None),
    (5.0,  2.0, False, None),
    (9.0,  3.0, True,  None),
    (10.0, 5.0, True,  None),
    (12.0, 5.0, False, None),
    # Float non natural
    (10.5, 5.25, True,  None),
    (10.5, 5.0, False,  None),
    # Ints
    (0,  1, True,  None),
    (1,  1, True,  None),
    (2,  1, True,  None),
    (4,  2, True,  None),
    (5,  2, False, None),
    (6,  3, True,  None),
    (9,  3, True,  None),
    (10, 5, True,  None),
    (12, 5, False, None),
    (17, 3, False, None),
    # Zeros
    (0,  1, True,  None), # This assumes 0 is a multiple of 1, technically True
    (1,  0, True,      ZeroDivisionError), # 1 is not a multiple of 0
    # None
    (None, 1,    None, TypeError),
    (1,    None, None, TypeError),
    # Strings
    ("A",  1,    None, TypeError),
    (1,    "A",  None, TypeError)]


@pytest.mark.parametrize("x, k, expectation, expected_error", testdata)
def test_is_multiple(x, k, expectation, expected_error):
    try:
        assert(is_multiple(x=x, k=k) == expectation)
    except:
        with pytest.raises(expected_error):
            assert(is_multiple(x=x, k=k) == expectation)
