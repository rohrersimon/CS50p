def main():
    while True:
        fraction = input("Fraction: ")
        fraction = fraction.split('/')

        try:
            fuel = int(fraction[0]) / int(fraction[1])
            if int(fraction[0]) > int(fraction[1]) or int(fraction[0]) < 0:
                continue
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            fuel = round(fuel * 100)

            if fuel <= 1:
                print("E")
            elif fuel >= 99:
                print("F")
            else:
                print(f"{fuel}%")
            break


def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()



