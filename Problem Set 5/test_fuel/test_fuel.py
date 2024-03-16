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


def test_convert():
    assert convert('99/100') == 99
    assert convert('1/100') == 1
    assert convert('1/5') == 20


def test_gauge_full():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'


def test_gauge_empty():
    assert gauge(1) == 'E'
    assert gauge(0) == 'E'


def test_gauge_percent():
    assert gauge(2) == '2%'
    assert gauge(98) == '98%'
#    for _ in range(10):
#        number = random.randint(2, 98)
#        assert gauge((number/100)) == (f"{number}%")
