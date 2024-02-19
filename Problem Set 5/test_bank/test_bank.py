from bank import value


def test_hello():
    assert value('hello') == 0
    assert value ('Hello') == 0


def test_h():
    assert value('h') == 20
    assert value('H') == 20
    assert value('Home') == 20


def test_non_h():
    assert value('absef') == 100
    assert value('!"£asANSDOFEI3KASDkasdf') == 100