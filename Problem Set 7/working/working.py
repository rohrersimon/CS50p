import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    if matches := re.fullmatch(r"([0-9][0-9]?):([0-5][0-9]) (AM|PM) to ([0-9][0-9]?):([0-5][0-9]) (AM|PM)", s):
        start_hour = validate_hour(matches.group(1))
        start_minute = validate_minute(matches.group(2))
        start_meridem = matches.group(3)
        end_hour = validate_hour(matches.group(4))
        end_minute = validate_minute(matches.group(5))
        end_meridem = matches.group(6)

    elif matches := re.fullmatch(r"([0-9][0-9]?) (AM|PM) to ([0-9][0-9]?) (AM|PM)", s):
        start_hour = validate_hour(matches.group(1))
        start_minute = 0
        start_meridem = matches.group(2)
        end_hour = validate_hour(matches.group(3))
        end_minute = 0
        end_meridem = matches.group(4)

    else:
        raise ValueError

    start_hour, start_minute = get_24time(start_hour, start_minute, start_meridem)
    end_hour, end_minute = get_24time(end_hour, end_minute, end_meridem)
    return format_24time(start_hour, start_minute, end_hour, end_minute)


"""
Returns hour and minute values in 24h format.
Handles corner cases with 12:00 am/pm.
"""
def get_24time(hour, minute, meridem):
    if meridem == 'AM' and hour == 12:
        hour = 0
    elif meridem == 'PM' and hour == 12:
        hour = 12
    elif meridem == 'PM':
        hour += 12

    return hour, minute


"""
Changes value from str to int.
Validates if int is in correct range: 0-12
Returns value as int.
"""
def validate_hour(s):
    try:
        s = int(s)
    except:
        raise ValueError

    if 0 <= s <= 12:
        return s
    else:
        raise ValueError


"""
Changes value from str to int.
Validates if int is in correct range: 0-59
Returns value as int.
"""
def validate_minute(s):
    if s.startswith('0'):
        s = s.replace('0', '', 1)
    try:
        s = int(s)
    except:
        raise ValueError

    if 0 <= s <= 59:
        return s
    else:
        raise ValueError


"""
Format the correct string from the int values.
"""
def format_24time(start_hour, start_minute, end_hour, end_minute):
    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"


if __name__ == "__main__":
    main()
