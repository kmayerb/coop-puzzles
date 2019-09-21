import pytest
from puzzles.count_nucs import count_nucs

#(input,expectation,error)
testdata = [
    ('ATTGGG',  '1 0 3 2', None),
    ('ATTGGGX', None, ValueError), # Raise error if non nucleotide letter
    ('attggg',   '1 0 3 2', None),  # accept lowercase as equiv
    ('attgggx', None, ValueError),
    (None, None, TypeError),
    (1234, None, TypeError),
    (['ATTGGG'], None, TypeError)
]

@pytest.mark.parametrize("x, expectation, expected_error", testdata)
def test_count_nucs(x, expectation, expected_error):
    try:
        nuc_count = count_nucs(x)
        assert nuc_count == expectation
    except:
        with pytest.raises(expected_error):
            nuc_count = count_nucs(x)
