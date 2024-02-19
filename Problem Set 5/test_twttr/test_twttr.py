from twttr import shorten

def test_letters():
    assert shorten('Kopenhagen') == 'Kpnhgn'
    assert shorten('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'


def test_numbers():
    assert shorten('1234567890') == '1234567890'


def test_special_characters():
    assert shorten('!"£$%^&*()_+') == '!"£$%^&*()_+'