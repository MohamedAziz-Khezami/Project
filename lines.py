import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")

else:
    nb = 0
    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("#") or len(line) == 0:
                    continue
                else:
                    nb += 1

            print(nb)

    except FileNotFoundError:
        sys.exit("File does not exist")
