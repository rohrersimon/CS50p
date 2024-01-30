expression = input("Expression: ").strip()
expression = expression.split()


x = float(expression[0])
z = float(expression[2])


match expression[1]:
    case "+":
        result = x + z
    case "-":
        result = x - z
    case "*":
        result = x * z
    case "/":
        result = x / z


print(result)
