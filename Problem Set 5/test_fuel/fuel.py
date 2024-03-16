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
            return fraction * 100


def gauge(fraction):
    if fraction <= 1:
        return "E"
    elif fraction >= 99:
        return "F"
    else:
        return (f"{fraction}%")


if __name__ == "__main__":
    main()



