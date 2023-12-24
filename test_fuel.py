from fuel import convert, gauge
import pytest


def test_fuel():
    assert gauge(convert("1/4")) == "25%"
    assert gauge(convert("0/1")) == "E"
    assert gauge(convert("1/100")) == "E"

    assert gauge(convert("99/100")) == "F"


def test_Errors():
    with pytest.raises(AttributeError):
        gauge(convert(3 / 4))

    with pytest.raises(ZeroDivisionError):
        gauge(convert("1/0"))

    with pytest.raises(ValueError):
        gauge(convert("3.5/3"))
