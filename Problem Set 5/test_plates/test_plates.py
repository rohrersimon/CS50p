import plates


def test_starts_with_two_letters():
    assert plates.is_valid('AA1111') == True
    assert plates.is_valid('ZZ1111') == True
    assert plates.is_valid('A91111') == False
    assert plates.is_valid('A11111') == False


def test_at_least_two_chars():
    assert plates.is_valid('AA') == True
    assert plates.is_valid('A') == False


def test_max_six_chars():
    assert plates.is_valid('AAAAAA') == True
    assert plates.is_valid('AAAAAAB') == False


def test_no_numbers_in_middle():
    assert plates.is_valid('AAA111') == True
    assert plates.is_valid('AA111A') == False
    assert plates.is_valid('111AAA') == False
    assert plates.is_valid('A111AB') == False


def test_first_number_not_zero():
    assert plates.is_valid('AA0999') == False
    assert plates.is_valid('AAZZ09') == False
    assert plates.is_valid('AABA0') == False
    assert plates.is_valid('CS05') == False


def test_no_special_chars():
    assert plates.is_valid('AA111$') == False
    assert plates.is_valid('A£A111') == False
    assert plates.is_valid('AA%111') == False
    assert plates.is_valid(';AA111') == False