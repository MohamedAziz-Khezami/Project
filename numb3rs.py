import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    search = re.search(r"^(\w{1,3})+\.(\w{1,3})+\.(\w{1,3})+\.(\w{1,3})+$", ip)
    if search:
        if (
            0 <= int(search.group(1)) <= 255
            and 0 <= int(search.group(2)) <= 255
            and 0 <= int(search.group(3)) <= 255
            and 0 <= int(search.group(4)) <= 255
        ):
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
