import pytest
from datetime import date, datetime, timedelta
import inflect
from seasons import format_input, get_minutes, write_in_words

def test_format_input():
    # Test expected values
    assert format_input('2024-02-28') == datetime(2024, 2, 28).date()
    assert format_input('2000-01-01') == datetime(2000, 1, 1).date()
    assert format_input('1999-12-31') == datetime(1999, 12, 31).date()

    # Test invalid values
    with pytest.raises(SystemExit):
        format_input('2090-02-30')
    with pytest.raises(SystemExit):
        format_input('2000-13-01')
    with pytest.raises(SystemExit):
        format_input('1999-12-32')

def test_get_minutes():
    # Test expected values
    assert get_minutes(datetime(2024, 2, 29).date()) == 0
    assert get_minutes(datetime.strptime('2024-02-29', '%Y-%m-%d').date() - timedelta(days=1)) == 24*60
    assert get_minutes(datetime.strptime('2024-02-29', '%Y-%m-%d').date() - timedelta(days=365)) == 365*24*60
    assert get_minutes(datetime.strptime('2023-03-01', '%Y-%m-%d').date()) == 365*24*60

    # Test invalid values
    with pytest.raises(SystemExit):
        get_minutes(datetime.strptime('2024-02-29', '%Y-%m-%d').date() + timedelta(days=1))
    with pytest.raises(SystemExit):
        get_minutes(datetime.strptime('2024-02-29', '%Y-%m-%d').date() + timedelta(days=30))
    with pytest.raises(SystemExit):
        get_minutes(datetime.strptime('2024-02-29', '%Y-%m-%d').date() + timedelta(days=365))

def test_write_in_words():
    # Test expected values
    assert write_in_words(0) == 'Zero minutes'
    assert write_in_words(1) == 'One minute'
    assert write_in_words(2) == 'Two minutes'

    # Test invalid values
    with pytest.raises(ValueError):
        write_in_words(-1)
    with pytest.raises(ValueError):
        write_in_words(-100)
    with pytest.raises(ValueError):
        write_in_words(-1000)
