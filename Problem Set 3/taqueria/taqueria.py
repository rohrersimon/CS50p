menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    bill = 0.00

    while True:
        try:
            userInput = input("Item: ").lower()
        except EOFError:
            print()
            exit()
        else:
            new_bill = calc_total(userInput, bill)
            if new_bill > bill:
                bill = new_bill
                print(f"Total: ${bill:.2f}")


def calc_total(userInput, number):
    for item in menu:
        if item.lower() == userInput:
            number += menu[item]

    return number

main()
