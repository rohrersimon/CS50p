amount_due = 50
amount_paid = 0

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Instert Coin: "))

    if coin == 5 or coin == 10 or coin == 25:
        amount_due -= coin
        amount_paid += coin

change = abs(amount_due)

print(f"Change Owed: {change}")
