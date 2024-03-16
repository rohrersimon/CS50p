# Password Strength Checker
This project is password strength checker. It evaluates your password for its complexity and gives it a score. It then prints out the results of the check to the console alongside some suggestions to improve your password.

[Video Demo](https://youtu.be/W1hjdY1bpUI)

# Dependencies
For the pip installable modules, please check the requirements.txt file. However, the 'PyEnchant' module requires installing local libraries that pip doesn't handle itself. **Without the word library installed separately, the program doesn't work!** In Debian based Linux it's a simple matter of `apt search libenchant` and then `sudo apt install libenchant-2-2`. Insert the correct package name there. Here's a link to the official installation instructions: https://pyenchant.github.io/pyenchant/install.html

# How it works
The password strength checker evaluates the password loosely based on the criteria mentioned in the [NIST Password Rule Book](https://www.isaca.org/resources/isaca-journal/issues/2019/volume-1/nists-new-password-rule-book-updated-guidelines-offer-benefits-and-risk). Criteria evaluated are:
- Length
- Contains upper case letter(s)
- Contains lower case letter(s)
- Contains special character(s)
- Contains number(s)
- Contains characters repeated at least 3x

I also included two special features:
- Checks if the password is an exact match in a list of the internet's 10'000 most popular passwords
- Recognises words in leet speech and converts those into normal words

# Design Choices
## PyEnchant module
The PyEnchant module is used to check if a string is an English dictionary word. It's technically a spell-checking module that I use for this alternative purpose. I originally used the PyMultiDictionary module that doesn't spell check but returns dictionary definitions. This worked as well but was significantly slower to the point that a password check would take several seconds to finish. I decided on the faster module PyEnchant with the drawback that its word library has to be installed separately.

## Object oriented programming
I tried hard to use OOP style for this program and even created three classes at some point: Password, PwdCheck, and LeetCheck. However, I would've simply hidden all my functions in different classes which don't use any instances. Only the Password class would've had one instance for the password entered. I've created regions in my code to group the functions that belong together instead.

# Sources
## NIST Password Rule Book
https://www.isaca.org/resources/isaca-journal/issues/2019/volume-1/nists-new-password-rule-book-updated-guidelines-offer-benefits-and-risk

## Password list source
https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt
