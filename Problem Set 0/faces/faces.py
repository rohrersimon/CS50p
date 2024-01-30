# Convert emoticon to emoji

def main():
    # userInput = "This is my test phrase. :) It's very boring :("
    userInput = input("Write a phrase with emoticon :) and :( ... ")
    userInput = convert(userInput)
    print(userInput)

def convert(phrase):
    return phrase.replace(":)", "🙂").replace(":(", "🙁")

main()
