# region imports
from project import *
import enchant

# endregion imports


# region global variables
passing_score = 6
dictionary = enchant.Dict("en_US")

## Suggestion messages
pop_suggestion = "Your password matches one of the most commonly used passwords. Try a more unique password."
len_suggestion1 = "Your password should have 12 characters or more."
len_suggestion2 = "A passphrase is a good way to create long passwords.\n   E.g. Tom&JenLookAfterDogsToday90 or WhisperingWillowTree336%"
upper_suggestion = "Include upper case letters into your password."
lower_suggestion = "Include lower case letters into your password."
digit_suggestion = "Include numbers into your password."
spec_suggestion = "Include special characters into your password."
repeat_suggestion = "Don't repeat the same character 3 or more times."
leet_suggestion = "You seem to have used leet speech to create a more complex password.\n   This technique is commonly used and has reduced your password score.\n   Use a more random approach instead."
# endregion global variables


# region checking functions
def test_check_length():
    assert check_length("1234567") == (False, 0)
    assert check_length("12345678") == (True, 0)
    assert check_length("123456789012") == (True, 1)
    assert check_length("12345678901234567") == (True, 1)
    assert check_length("123456789012345678") == (True, 2)
    assert check_length("12345678901234567890123") == (True, 2)
    assert check_length("123456789012345678901234") == (True, 3)
    assert check_length("12345678901234567890123456789012") == (True, 4)


def test_check_uppercase():
    assert check_uppercase("Asdkofwe") == 1
    assert check_uppercase("sdkoTfwe") == 1
    assert check_uppercase("sdkofwe") == 0
    assert check_uppercase('asd"£$-') == 0
    assert check_uppercase("asdfWgg£%$_") == 1
    assert check_uppercase("     D   ") == 1


def test_check_lowercase():
    assert check_lowercase("Asdkofwe") == 1
    assert check_lowercase("     D   ") == 0
    assert check_lowercase('"£$*$^754S"') == 0
    assert check_lowercase('"£$-03AxASD@"') == 1
    assert check_lowercase("   a    ") == 1


def test_check_digits():
    assert check_digits("Asdkofwe") == 0
    assert check_digits("     D   ") == 0
    assert check_digits('"£$*$^754S"') == 1
    assert check_digits('"£$-03AxASD@"') == 1
    assert check_digits("sdk2oTfwe") == 1
    assert check_digits('asd"£$-') == 0
    assert check_digits("asdfWgg£%$_") == 0
    assert check_digits("     0   ") == 1


def test_check_special_characters():
    assert check_special_characters("Asdkofwe") == 0
    assert check_special_characters("0092jADF~") == 1
    assert check_special_characters('"£$*$^754S"') == 1
    assert check_special_characters('"£$-03AxASD@"') == 1
    assert check_special_characters("sdk2oTfwe") == 0
    assert check_special_characters('asd"£$-') == 1
    assert check_special_characters("asdfWgg£%$_") == 1
    assert check_special_characters("asdf¬adf") == 1


def test_check_repetition():
    assert check_repetition('aabbccDDD"£$') == (True, 1)
    assert check_repetition("anei&Dk00a0SDf02") == (False, 0)
    assert check_repetition("anei&&&asndW") == (True, 1)
    assert check_repetition("anei&Dk00a0SDf02") == (False, 0)
    assert check_repetition("a111111nei&Dk00a0SDf02") == (True, 1)
    assert check_repetition("anei&D00k00a0SDf02") == (False, 0)
    assert check_repetition("00000000000") == (True, 1)


def test_check():
    assert check("Password123!") == (6, [])
    assert check("Password123!123456") == (7, [])
    assert check("password123!123456") == (6, [upper_suggestion])
    assert check("Password123") == (
        0,
        [
            pop_suggestion,
            len_suggestion1,
            len_suggestion2,
            spec_suggestion,
        ],
    )
    assert check("Pa1!£z0") == (0, [len_suggestion1, len_suggestion2])
    assert check("aB%000000000") == (5, [repeat_suggestion])


def test_check_popularity():
    assert check_popularity("jordan") == True
    assert check_popularity("MyChrazyPassword7000!$") == False


# endregion checking functions


# region leet functions
def test_is_word():
    assert is_word("hello") == True
    assert is_word("hopeful") == True
    assert is_word("h3110") == False
    assert is_word("h0p3fu7") == False


def test_leet_to_word():
    assert leet_to_word(["h0p3", "T0wn", "7h0R"]) == ["hope", "Town", "thoR"]
    assert leet_to_word(["1", "2", "3", "4"]) == ["i", "z", "e", "a"]


def test_find_potential_leet_words():
    assert find_potential_leet_words("h0p3 $13rr4") == [(0, 4), (5, 11)]
    assert find_potential_leet_words("1234&&***") == [(0, 4)]
    assert find_potential_leet_words("!£$%*090972asdASF") == [(5, 17)]
    assert find_potential_leet_words("!2309a;;") == [(1, 6)]


def test_sliding_window():
    assert sliding_window("££$7r3ng7h77777&&", [(2, 15)]) == [(2, 10)]
    assert sliding_window("££Rhy7hm77777&&", [(2, 13)]) == [(2, 8)]
    assert sliding_window("££Glyph77777&&", [(2, 12)]) == [(2, 7)]


def test_get_str_from_index():
    assert get_str_from_index("$$$Arrakis&&&", [(3, 10), (4, 6)]) == ["Arrakis", "rr"]


def test_replace_leet_words():
    assert replace_leet_words("P4$$w0rd234!", [(0, 8)]) == "Password234!"


def test_replace():
    assert replace("MyCr4zyP4$$w0rd234££") == "MyCrazyPassword234££"
    assert replace("**7h0r!!!") == "**thor!!!"


# endregion leet functions
