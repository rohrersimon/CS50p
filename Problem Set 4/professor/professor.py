import random


def main():
    score = 0
    level = get_level()

    for i in range(10):
        if run_exercise(level):
            score += 1

    print(f"Score: {score}")


def run_exercise(level):
    x = generate_integer(level)
    y = generate_integer(level)
    attempt = 0

    while True:
        answer = input(f"{x} + {y} = ")
        try:
            answer = int(answer)
        except:
            pass
        else:
            if answer == x + y:
                return True

        print("EEE")
        if attempt >= 2:
            print(f"{x} + {y} = {x + y}")
            return False
        attempt += 1


def get_level():
    while True:
        level = input("Level: ")
        try:
            level = int(level)
        except:
            pass
        else:
            if level == 1 or level == 2 or level == 3:
                return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
