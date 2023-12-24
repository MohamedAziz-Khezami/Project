import sys
import csv


def command_line_check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") == False or sys.argv[2].endswith(".csv") == False:
        sys.exit("Not a csv file")


def reading():
    students = []
    try:
        with open(sys.argv[1]) as file_1:
            reader = csv.DictReader(file_1)
            for line in reader:
                last, first = line["name"].split(",")
                students.append(
                    {"first": first.lstrip(), "last": last, "house": line["house"]}
                )
        return students

    except FileNotFoundError:
        sys.exit("Could not read " + sys.argv[1])


def writing(students):
    with open(sys.argv[2], "w") as file_2:
        writer = csv.DictWriter(file_2, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in students:
            writer.writerow(
                {"first": row["first"], "last": row["last"], "house": row["house"]}
            )


def main():
    command_line_check()
    writing(reading())


main()