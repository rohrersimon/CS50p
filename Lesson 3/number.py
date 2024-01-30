while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print('x is not a number (integer)')
    else:
        break

print(f"x is {x}")

### OR ###

while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print('x is not a number (integer)')

print(f"x is {x}")
