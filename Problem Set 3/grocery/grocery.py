def main():
    grocery_list = {}
    while True:
        try:
            item = input().upper()
        except EOFError:
            print_list(grocery_list)
            print()
            break
        else:
            grocery_list = add_list(grocery_list, item)


def add_list(dictionary, item):
    if dictionary.get(item) == None:
        dictionary[item] = 1
    else:
        dictionary[item] = dictionary[item] + 1


    return dictionary


def print_list(dictionary):
    keys = sorted(dictionary.keys())
    for item in keys:
        print(f"{dictionary.get(item)} {item}")


main()
