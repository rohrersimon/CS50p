import pytest
from um import count


def test_count():
    assert count("hello, um, world") == 1
    assert count("yummy") == 0
    assert count("Um, um, UM") == 3
    assert count("ummm") == 0
    assert count("some random text") == 0