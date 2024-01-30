word = input('Input: ')

for letter in word:
    match letter.lower():
        case 'a' | 'e' | 'i' | 'o' | 'u':
            word = word.replace(letter, '')
        case _:
            continue

print(f'Output: {word}')
