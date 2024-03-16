# region imports
from rich import print
import platform
import os
from math import floor
import re
import enchant
import json
import sys

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
def check_length(password: str) -> tuple[bool, int]:
    """
    Checks length requirement.

    :param password: Password to be checked
    :type password: str
    :return: Tuple, bool if password is longer than 12 characters, int with strength score increase (0 to infinite).
    :rtype: tuple
    """
    length = len(password)
    if length < 8:
        return False, 0
    if length < 12:
        return True, 0
    else:
        return True, floor((length - 12) / 6) + 1


def check_uppercase(password: str) -> bool:
    """
    Checks for uppercase letters.

    :param password: Password to be checked
    :type password: str
    :return: Bool if password contains uppercase letters.
    :rtype: bool
    """
    if re.search(r"[A-Z]", password):
        return True
    else:
        return False


def check_lowercase(password: str) -> bool:
    """
    Checks for lowercase letters.

    :param password: Password to be checked
    :type password: str
    :return: Bool if password contains lowercase letters.
    :rtype: bool
    """
    if re.search(r"[a-z]", password):
        return True
    else:
        return False


def check_digits(password: str) -> bool:
    """
    Checks for digits.

    :param password: Password to be checked
    :type password: str
    :return: Bool if password contains numbers letters.
    :rtype: bool
    """
    if re.search(r"\d", password):
        return True
    else:
        return False


def check_special_characters(password: str) -> bool:
    """
    Checks for special characters.

    :param password: Password to be checked
    :type password: str
    :return: Bool if password contains special characters.
    :rtype: bool
    """
    if re.search(r"\W", password):
        return True
    else:
        return False


def check_popularity(password: str) -> bool:
    """
    Checks for an exact match in a list of 10'000 popular passwords.

    :param password: Password to be checked
    :type password: str
    :return: Bool if password is found in the popular_passwords list.
    :rtype: bool
    """
    try:
        with open("popular_passwords.json", "r") as file:
            lines = json.load(file)
    except FileNotFoundError:
        sys.exit(
            "Error: The file popular_passwords.json could not be found. Make sure it's in the program directory."
        )

    if password in lines:
        return True
    else:
        return False


def check_repetition(password: str) -> tuple[bool, int]:
    """
    Checks for symbols repeated 3x or more.

    :param password: Password to be checked
    :type password: str
    :return: Tuple, bool if password contains symbols repeated 3x or more, int how many times pattern of 3x same symbol was found.
    :rtype: tuple[bool, int]
    """
    regex = r"(.)\1{2,}"
    matches: int = len(re.findall(regex, password))
    if matches > 0:
        return True, matches
    else:
        return False, matches


def check(password: str) -> tuple[int, list]:
    """
    Main password checking function: calls all the other checking functions.
    Checks the complexity of a password. It gives a complexity score and suggestions based on found weaknesses.

    :param password: Password to be checked
    :type password: str
    :return: Tuple, int complexity score, list with improvement suggestions based on found weaknesses.
    :rtype: tuple[bool, int]
    """
    complexity_score = 0
    suggestions: list = []
    score_be_zero = False

    if check_popularity(password):
        suggestions.insert(0, pop_suggestion)
        score_be_zero = True

    long_enough, lenth_score = check_length(password)
    if long_enough:
        complexity_score += lenth_score
    else:
        score_be_zero = True

    if lenth_score < 1:
        suggestions.append(len_suggestion1)
        suggestions.append(len_suggestion2)

    if check_uppercase(password):
        complexity_score += 1
    else:
        suggestions.append(upper_suggestion)

    if check_lowercase(password):
        complexity_score += 1
    else:
        suggestions.append(lower_suggestion)

    if check_digits(password):
        complexity_score += 1
    else:
        suggestions.append(digit_suggestion)

    if check_special_characters(password):
        complexity_score += 1
    else:
        suggestions.append(spec_suggestion)

    got_repetitions, number_repetitions = check_repetition(password)
    if got_repetitions:
        complexity_score -= number_repetitions - 1
        suggestions.append(repeat_suggestion)
    else:
        complexity_score += 1

    if score_be_zero:
        complexity_score = 0

    return complexity_score, suggestions


# endregion checking functions


# region printing funcitons
def print_suggestions(suggestion_list: list) -> None:
    """
    Prints a message to the terminal that suggests where the password can be improved.

    :param suggestion_list: List of improvement suggestions.
    :type suggestion_list: list
    :return: None
    :rtype: None
    """
    print()
    print(f"[bold]The following suggestions can improve your score[/] :rocket:")
    for suggestion in suggestion_list:
        if suggestion.startswith("Your password matches"):
            print(f" [bold yellow]-[/] [red]{suggestion}[/]")
        elif suggestion.startswith("You seem to have used leet speech"):
            print(f" [bold green]-[/] [yellow]{leet_suggestion}[/]")
        else:
            print(f" [bold green]-[/] {suggestion}")


def print_score(has_passed: bool, the_score: int) -> None:
    """
    Prints a message to the terminal that reveals the password score.

    :param has_passed: Bool if the password complexity score reaches the passing score threshold
    :type has_passed: Bool
    :param the_score: int, the complexity score of the password
    :type the_score: int
    :return: None
    :rtype: None
    """
    if has_passed:
        result = "[bold green]SUCCEEDED[/]"
    else:
        result = "[bold red]FAILED[/]"

    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    print(f"[bold]Your password has {result} the test with a score of {the_score}.[/]")
    print(f"The minimum, passing score is {passing_score}.")


# endregion printing functions


# region leet functions
def is_word(word: str) -> bool:
    """
    Checks if given input is a word by checking a dictionary.

    :param word: Word to be checked if it appears in the dictionary.
    :type word: str
    :return: Bool if word is in dictionary.
    :rtype: bool
    """
    if dictionary.check(word):
        return True
    else:
        return False


def leet_to_word(leet_word_list: list) -> list:
    """
    Replaces common symbols used in leet speech with letters.

    :param leet_word_list: List of all the leet speech words.
    :type leet_word_list: list
    :return: List of all the letter words.
    :rtype: list
    """
    leet_dict = {
        "4": "a",
        "8": "b",
        "3": "e",
        "1": "i",
        "0": "o",
        "5": "s",
        "7": "t",
        "2": "z",
        "$": "s",
    }

    clear_word_list = []

    for leet_word in leet_word_list:
        clear_word = ""

        for i in range(len(leet_word)):
            character = leet_word[i]
            if character in leet_dict:
                clear_word += leet_dict[character]
            else:
                clear_word += leet_word[i]

        clear_word_list.append(clear_word)

    return clear_word_list


def find_potential_leet_words(password: str) -> list:
    """
    Checks a str for potential leet speech words.
    This is a achieved by checking for a pattern of letters and leet speech symbols.

    :param password: Str that is to be checked for leet speech words.
    :type password: str
    :return: List of index tubples that indicate all potential leet speech words in password.
    :rtype: list
    """
    regex = r"([a-zA-Z0-9$]{2,})"
    _indeces = []

    matches = re.finditer(regex, password)
    for match in matches:
        _indeces.append(match.span())

    return _indeces


def sliding_window(leet_word: str, indexes: list) -> list:
    """
    Changes a str from leet speech to normal letters.
    Then checks that str for dictionary words.
    Returns the indexes of the dictionary words.

    :param leet_word: Str that is a password containing leet speech style.
    :type leet_word: str
    :param indexes: List of index tuples that indicate potential leet speech substrings.
    :type indexes: list
    :return: List of index tubples that indicate all actual leet speech words.
    :rtype: list
    """
    w_size = 3  # Minimum window size
    clear_word = (leet_to_word([leet_word]))[0]  # [0] unpacks list containing one str

    # potential_leet_words: List of potential leet words tupled with the starting indexes of each word from password/clear_word
    potential_leet_words = [
        (word, clear_word.index(word))
        for word in leet_to_word(get_str_from_index(clear_word, indexes))
    ]
    new_indeces = []  # Index tuples indicating actual leet speech words

    for word, start_index in potential_leet_words:
        length = len(word)
        for i in range(  # i = current window size, size reducing by -1 each loop
            length, (w_size - 1), -1
        ):
            for j in range(length - i + 1):  # j = window start index
                if is_word(word[j : j + i]):
                    new_indeces.append((start_index + j, start_index + j + i))

    return new_indeces


def get_str_from_index(password: str, indexes: list) -> list:
    """
    Returns all the substrings of the password indicated by the indexes list.

    :param password: Str that is the password.
    :type password: str
    :param indexes: List of index tuples that indicate substrings of the password.
    :type indexes: list
    :return: List of password substrings indicated by the indexes list.
    :rtype: list
    """
    word_list = []
    for start, end in indexes:
        sub_string = password[start:end]
        word_list.append(sub_string)

    return word_list


def replace_leet_words(password: str, indexes: list) -> str:
    """
    Returns the same str with leet speech substrings replaced with corresponding lettered words.
    Leet speech substrings need to be indicated by the indexes list.

    :param password: Str that is the password.
    :type password: str
    :param indexes: List of index tuples that indicate actual leet speech substrings in the password.
    :type indexes: list
    :return: Str of password where leet speech substrings have been replaced with letter words.
    :rtype: str
    """
    word_list = list(password)

    for start, end in indexes:
        leet_word = password[start:end]
        clear_word = leet_to_word(leet_word)
        word_list[start:end] = clear_word

    clear_word = "".join(word_list)
    return clear_word


def replace(password: str) -> str:
    """
    Main leet speech checking function: calls all the other leet speech functions.
    Replaces leet speech substrings in a str (password) with their lettered counterpars.

    :param password: Str that is the password.
    :type password: str
    :return: Str of password where leet speech substrings have been replaced with letter words.
    :rtype: str
    """
    # Analize password for non-special character substrings
    # Return indexes of those substrings
    indices = find_potential_leet_words(password)

    # Convert those substrings from leet speech to lettered strings
    # Check those lettered strings for actual words
    # Return indexes of the actual words which in the original password are leet speech words
    indices = sliding_window(password, indices)

    # Take password and replace leet speech words with actual words
    # Return this new version of the password for complexity score analysis
    return replace_leet_words(password, indices)


# endregion leet functions


# region main
def main() -> None:
    """
    1. Prompts the user for a password.
    2. Replaces leet speech substrings found in the password with lettered words.
    3. Analyses this new version of the password for complexity and gives it a score.
    4. The password passes the test if it reaches the paspopular_passwordssing score or more.
    5. Prints out the result of the test.
    6. Prints suggestions about how to improve the password further if weaknesses were found: e.g. no special characters.
    """
    password = input("Enter your password: ").strip()
    no_leet_password = replace(password)

    leet_score, leet_suggestions = check(password)
    no_leet_score, no_leet_suggestions = check(no_leet_password)

    if no_leet_score < leet_score:
        leet = True
        try:
            no_leet_suggestions.remove(digit_suggestion)
        except ValueError:
            pass
        if no_leet_suggestions is not None:
            no_leet_suggestions.insert(0, leet_suggestion)
        else:
            no_leet_suggestions = [leet_suggestion]
    else:
        leet = False

    if leet_score >= passing_score and no_leet_score >= passing_score:
        passed = True
    elif no_leet_score >= passing_score and leet_score < passing_score:
        passed = True
    elif leet_score >= passing_score and no_leet_score < passing_score:
        passed = False
    else:
        passed = False

    print_score(passed, no_leet_score)
    if passed and len(leet_suggestions) != 0:
        print_suggestions(leet_suggestions)
    elif leet and len(leet_suggestions) != 0:
        print_suggestions(no_leet_suggestions)
    elif len(leet_suggestions) != 0:
        print_suggestions(leet_suggestions)


if __name__ == "__main__":
    main()


# endregion main
