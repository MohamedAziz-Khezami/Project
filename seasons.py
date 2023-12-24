import inflect

import sys, re
from datetime import datetime
from datetime import date


p = inflect.engine()


def transf(b_date):
    matches = re.search(r"^(\d){4}-(\d){2}-(\d){2}$", b_date)

    if matches and datetime.strptime(b_date, "%Y-%m-%d").date() <= date.today():
        y, m, d = b_date.split("-")
        b_date = date(int(y), int(m), int(d))

        total_minutes = (date.today() - b_date).days * 24 * 60

        word_representation = p.number_to_words(total_minutes, andword="") + " minutes"

        return word_representation.capitalize()

    else:
        sys.exit("Invalid date")


def main():
    print(transf(input("Date of birth: ")))


if __name__ == "__main__":
    main()
