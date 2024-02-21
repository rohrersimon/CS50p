def main():
    greeting = input("Write a greeting: ")
    money = value(greeting)
    print(f"${money}")


def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith('h'):
        if greeting.startswith('hello'):
            money = 0
        else:
            money = 20
    else:
        money = 100
    return money


if __name__ == "__main__":
    main()

## comment
    
"""
Mydocstring
"""