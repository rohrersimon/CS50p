months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        date = input("Date: ").strip()
        valid_input = reformat_date(date)
        if valid_input:
            break


def reformat_date(date):
    index = 0

    has_month = False
    for month in months:
        if month in date:
            has_month = True
            break
        index += 1

    if ' ' in date:
        has_space = True
    else:
        has_space = False

    if '/' in date:
        has_slash = True
    else:
        has_slash = False

    if ',' in date:
        has_comma = True
    else:
        has_comma = False

    if has_slash and has_space == False and has_month == False and has_comma == False:
        return print_slashes(date)
    elif has_slash == False and has_space and has_month and has_comma:
        return print_written(date, index)
    else:
        return False


def print_slashes(date):
    date_list = date.split('/')

    if len(date_list) != 3:
        return False

    try:
        day = int(date_list[1])
        month = int(date_list[0])
        year = int(date_list[2])
    except ValueError:
        return False

    if valid_date(year, month, day):
        print(f"{year}-{month:02}-{day:02}")
        return True
    else:
        return False


def print_written(date, index):
    date_list = date.split(" ")
    month = index + 1
    day_list = date_list[1].split(",")

    try:
        day =  int(day_list[0])
        year = int(date_list[2])
    except ValueError:
        return False

    if valid_date(year, month, day):
        reformatted_date = f"{year}-{month:02}-{day:02}"
        print(reformatted_date)
        return True
    else:
        return False


def valid_date(year, month, day):
    if year < 0 or year > 9999:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False

    return True


main()

# Handle: October/9/1701
# And: September 8 1636
