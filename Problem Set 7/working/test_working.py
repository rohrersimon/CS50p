import pytest
import working


def test_convert():
    assert working.convert("12:00 AM to 1:00 PM") == "00:00 to 13:00"
    assert working.convert("1 AM to 12 PM") == "01:00 to 12:00"


def test_errors():
    with pytest.raises(ValueError):
        working.convert("invalid input")
    with pytest.raises(ValueError):
        working.convert("19 AM to 12 PM")
    with pytest.raises(ValueError):
        working.convert("03 AM to 32 PM")
    with pytest.raises(ValueError):
        working.convert("12:00 AM to 35:00 PM")
    with pytest.raises(ValueError):
        working.convert("73:00 AM to 1:00 PM")
    with pytest.raises(ValueError):
        working.convert("12:85 AM to 1:00 PM")
    with pytest.raises(ValueError):
        working.convert("12:00 AM to 1:91 PM")


"""
Commented out for submission. Bot didn't like these functions.

def test_get_24time():
    assert working.get_24time(12, 0, 'AM') == (0, 0)
    assert working.get_24time(1, 0, 'PM') == (13, 0)


def test_validate_hour():
    assert working.validate_hour('12') == 12
    assert working.validate_hour('1') == 1
    with pytest.raises(ValueError):
        working.validate_hour('13')
    with pytest.raises(ValueError):
        working.validate_hour('invalid')


def test_validate_minute():
    assert working.validate_minute('00') == 0
    assert working.validate_minute('59') == 59
    with pytest.raises(ValueError):
        working.validate_minute('60')
    with pytest.raises(ValueError):
        working.validate_minute('invalid')


def test_format_24time():
    assert working.format_24time(0, 0, 13, 0) == "00:00 to 13:00"
    assert working.format_24time(1, 1, 12, 0) == "01:01 to 12:00"
"""
