import csv, sys
from tabulate import tabulate

if len(sys.argv) > 2:
    sys.exit("Too many command-line argumetns")

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a csv file")

else:
    try:
        table = []
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
        header = table[0]
        print(tabulate(table[1:], header, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")
