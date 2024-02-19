def main():
    while True:
        fraction = input("Fraction: ")
        percentage = convert(fraction)
        print (gauge(percentage))


def convert(fraction):
    fraction = fraction.split('/')

    try:
        fuel = int(fraction[0]) / int(fraction[1])
        #if int(fraction[0]) > int(fraction[1]) or int(fraction[0]) < 0:
        #    continue
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

    return fuel


def gauge(percentage):
    percentage = round(percentage * 100)

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (f"{percentage}%")


if __name__ == "__main__":
    main()



