from datetime import date, datetime, timedelta
import sys, inflect


p = inflect.engine()


def main():
    user_input = input('Date of Birth: ')

    try:
        birth_date = datetime.strptime(user_input, '%Y-%m-%d').date()
    except ValueError:
        sys.exit('Invalid date')

    minutes = get_minutes(birth_date)
    print(minutes)


def get_minutes(any_date):
    time_difference = date.today() - any_date
    minutes = time_difference.days * 24 * 60

    if minutes >= 0:
        return (p.number_to_words(minutes, andword='')).capitalize() + ' ' + p.plural('minute', minutes)
    else:
        sys.exit('Invalid date')


if __name__ == "__main__":
    main()
