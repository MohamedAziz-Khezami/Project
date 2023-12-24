from validator_collection import checkers


def main():
    print(email_check(input("What is your email? ")))


def email_check(s):
    if checkers.is_email(s, force_run=True):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
