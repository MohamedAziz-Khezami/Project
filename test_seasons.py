from seasons import transf

import pytest


def test_transf():
    assert transf("1999-01-01") == "Twelve million, eight hundred eighty-six thousand, five hundred sixty minutes"
    assert transf("2003-09-07") == "Ten million, four hundred twenty-four thousand, one hundred sixty minutes"
def test_invalid_input_transf():
        with pytest.raises(SystemExit):
            transf("200-01-20")
