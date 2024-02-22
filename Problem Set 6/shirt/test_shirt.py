from shirt import get_format

def test_get_format():
    assert get_format('anoesi.png') == 'png'
    assert get_format('anoesi.jpg') == 'jpg'
    assert get_format('anoesi.jpeg') == 'jpg'
    assert get_format('anoesi.csv') == 'Invalid input'