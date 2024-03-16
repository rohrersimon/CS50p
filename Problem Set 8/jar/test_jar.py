from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    assert Jar().deposit(1).size == 1
    assert Jar().deposit(12).size == 12

    with pytest.raises(ValueError):
        Jar().deposit(0)
    with pytest.raises(ValueError):
        Jar().deposit(-1)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    assert jar.withdraw(1).size == 11
    assert jar.withdraw(11).size == 0

    with pytest.raises(ValueError):
        jar.withdraw(0)
    with pytest.raises(ValueError):
        jar.withdraw(-1)
