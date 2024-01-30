from pyfiglet import Figlet
from sys import argv, exit
from random import randrange


figlet = Figlet()  # 549 fonts
fonts = figlet.getFonts()


if len(argv) == 1:
    index = randrange(548)
    f = fonts[index]
    figlet.setFont(font=f)
elif len(argv) == 3:
    if argv[1] == "-f" or argv[1] == "--font":
        f = argv[2]
        try:
            figlet.setFont(font=f)
        except:
            exit("Invalid usage")
    else:
        exit("Invalid usage")
else:
    exit("Invalid usage")


user_input = input("Input: ")
print(figlet.renderText(user_input))
