from datetime import date
import sys
import inflect


def main():
    inp= input("Date of Birth: ")
    dob = get_DOB(inp)
    print(get_minutes(dob))


def get_minutes(dob):
    p = inflect.engine()
    diff=date.today()-dob
    pristr=p.number_to_words(int(diff.days)*24*60).capitalize().replace(" and ", " ")+" minutes"

    return pristr


def get_DOB(inp):
    try:
        year, month, day = inp.split("-")
        return date(int(year), int(month), int(day))
    except :
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
