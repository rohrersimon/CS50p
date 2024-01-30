userInput = input("What's the answer to the Great Question of Life? ").lower().strip()

match userInput:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
