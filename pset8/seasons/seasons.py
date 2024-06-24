from datetime import date
import inflect
import sys


def main():
    dob = input("Date of Birth: ")
    print(get_minutes(dob))


def get_minutes(dob):
    dob = dob.strip().split("-", 3)

    if len(dob[0]) != 4 or len(dob[1]) != 2 or len(dob[2]) != 2:
        sys.exit(1)
    else:
        try:
            dob = date(int(dob[0]), int(dob[1]), int(dob[2]))
            current = date.today()

            num = (current - dob).days
            num = num * 1440
            p = inflect.engine()
            word = p.number_to_words(num, andword="")

            return word.strip().capitalize() + " minutes"
        except ValueError:
            sys.exit(1)


if __name__ == "__main__":
    main()
