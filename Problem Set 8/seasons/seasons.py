from datetime import date, datetime
import sys, inflect


p = inflect.engine()


def main():
    user_input = input('Date of Birth: ')
    birth_date = format_input(user_input)
    minutes = get_minutes(birth_date)
    words = write_in_words(minutes)
    print(words)


def format_input(date_string):
    try:
        return datetime.strptime(date_string, '%Y-%m-%d').date()
    except ValueError:
        sys.exit('Invalid date')


def get_minutes(date_object):
    time_difference = date.today() - date_object
    minutes = time_difference.days * 24 * 60

    if minutes >= 0:
        return minutes
    else:
        sys.exit('Invalid date')


def write_in_words(int):
    if int < 0:
        raise ValueError("Input must be non-negative")

    return (p.number_to_words(int, andword='')).capitalize() + ' ' + p.plural('minute', int)


if __name__ == "__main__":
    main()
