import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        level = input("Level: ")
        if level.isdigit() and 1 <= int(level) <= 3:
            return int(level)
        else:
            continue


def generate_integer(level):
    score = 0
    for _ in range(1, 11):
        if level == 1:
            a = random.randint(0, 9)
            b = random.randint(0, 9)
        elif level == 2:
            a = random.randint(10, 99)
            b = random.randint(10, 99)
        elif level == 3:
            a = random.randint(100, 999)
            b = random.randint(100, 999)
        c = a + b
        i = 1
        while i <= 3:
            answer = input(f"{a} + {b} = ")
            if answer.isdigit() and int(answer) == c:
                score += 1
                break
            else:
                print("EEE")
                i += 1
        if i>3:
            print(f"{a} + {b} = {c}")

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
