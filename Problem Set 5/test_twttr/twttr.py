def main():
    word = input('Input: ')
    word = shorten(word)
    print(f'Output: {word}')


def shorten(word):
    for letter in word:
        match letter.lower():
            case 'a' | 'e' | 'i' | 'o' | 'u':
                word = word.replace(letter, '')
            case _:
                continue
    return word


if __name__ == "__main__":
    main()