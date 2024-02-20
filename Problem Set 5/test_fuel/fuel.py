def main():
    user_input = input("Fraction: ")
    fraction = convert(user_input)
    print (gauge(fraction))


def convert(fraction_string):
    fraction_list = fraction_string.split('/')

    try:
        fraction = int(fraction_list[0]) / int(fraction_list[1])
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError
    else:
        if fraction > 1:
            raise ValueError
        else:
            return fraction


def gauge(fraction):
    percentage = round(fraction * 100)

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (f"{percentage}%")


if __name__ == "__main__":
    main()



