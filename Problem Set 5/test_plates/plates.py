def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if no_special_char(s) != True:
        return False

    if correct_length(s) != True:
        return False

    if letter_start(s) != True:
        return False

    if correct_numbers(s) != True:
        return False

    return True


def letter_start(word):
    for i in range(2):
        if word[i].isalpha() != True:
            return False
    return True


def correct_length(word):
    if 2 <= len(word) <= 6:
        return True
    return False


def correct_numbers(word):
    if zero_start(word):
        return False
    else:
        index = 0
        for i in word:
            if i.isdecimal():
                break
            index += 1

        for i in range(index, len(word)):
            if word[i].isalpha():
                return False

        return True


def no_special_char(word):
    if word.isalnum():
        return True
    else:
        return False


def zero_start(word):
    list = []

    for i in word:
        if i.isdecimal():
            list.append(int(i))

    if list == []:
        return False

    if list[0] == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
