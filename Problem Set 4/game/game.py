from random import randint


while True:
    max = input("Level: ")
    try:
        max = int(max)
    except:
        pass
    else:
        if max > 0:
            break


number = randint(1, max)
while True:
    guess = input("Guess: ")
    try:
        guess = int(guess)
    except:
        pass
    else:
        if guess < 0:
            continue
        elif guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        elif guess == number:
            print("Just right!")
            exit()



