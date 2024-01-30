import inflect


p = inflect.engine()
names = []

while True:
    try:
        user_input = input("Input: ")
    except EOFError:
        break
    else:
        names.append(user_input)

print()
print(f"Adieu, adieu, to {p.join(names)}")
