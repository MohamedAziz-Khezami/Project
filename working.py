import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(
        r"(1[0-2]|[1-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[1-9])(:[0-5][0-9])? (AM|PM)",
        s,
    )
    if matches:
        if matches.group(2) != None:
            if matches.group(3) == "AM":
                if matches.group(1) == "12":
                    first = "00" + (matches.group(2))
                else:
                    first = f"{int(matches.group(1)):02}" + matches.group(2)

            elif matches.group(3) == "PM":
                if matches.group(1) == "12":
                    first = "12" + (matches.group(2))
                else:
                    first = f"{(int(matches.group(1))+12):02}" + (matches.group(2))

            if matches.group(6) == "AM":
                if matches.group(4) == "12":
                    second = "00" + " to " + (matches.group(5))
                else:
                    second = f"{int(matches.group(4)):02}" + (matches.group(5))
            elif matches.group(6) == "PM":
                if matches.group(4) == "12":
                    second = "12" + (matches.group(5))
                else:
                    second = f"{(int(matches.group(4))+12):02}" + (matches.group(5))

            return first + " to " + second

        elif matches.group(2) == None:
            if matches.group(3) == "AM":
                if matches.group(1) == "12":
                    first = "00"
                else:
                    first = f"{int(matches.group(1)):02}"

            elif matches.group(3) == "PM":
                if matches.group(1) == "12":
                    first = "12"
                else:
                    first = f"{(int(matches.group(1))+12):02}"

            if matches.group(6) == "AM":
                if matches.group(4) == "12":
                    second = "00"
                else:
                    second = f"{int(matches.group(4)):02}"
            elif matches.group(6) == "PM":
                if matches.group(4) == "12":
                    second = "12"
                else:
                    second = f"{(int(matches.group(4))+12):02}"

            return first + ":00" + " to " + second + ":00"

    else:
        raise ValueError("Error")


if __name__ == "__main__":
    main()
