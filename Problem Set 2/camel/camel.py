user_input = input("camelCase: ").strip()

for letter in user_input:
    if letter.isupper():
        low_letter = letter.lower()
        user_input = user_input.replace(letter, "_" + low_letter)

print(f"snake_case: {user_input}")
