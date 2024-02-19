from fuel import convert, gauge

def test_convert_valueerror():
    assert convert('5/3')