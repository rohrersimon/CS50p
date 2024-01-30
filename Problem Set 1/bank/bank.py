greeting = input("Write a greeting: ").lower().strip()

if greeting.startswith('h'):
    if greeting.startswith('hello'):
        money = 0
    else:
        money = 20
else:
    money = 100

print(f"${money}")
