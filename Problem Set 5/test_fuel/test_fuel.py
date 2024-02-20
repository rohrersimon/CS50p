from fuel import convert, gauge
import pytest
import random

def test_convert_valueerror():
    with pytest.raises(ValueError):
        convert('cat/3')
        convert('9/4')


def test_convert_zerodevision():
    with pytest.raises(ZeroDivisionError):
        convert('3/0')


def test_gauge_full():
    assert gauge(0.99) == 'F'
    assert gauge(1) == 'F'
    assert gauge(400) == 'F'


def test_gauge_empty():
    assert gauge(0.01) == 'E'
    assert gauge(0) == 'E'


def test_gauge_percent():
    for _ in range(10):
        number = random.randint(0, 100)
        assert gauge((number/100)) == (f"{number}%")