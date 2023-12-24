def main():
    time=input("What time is it? ")

    if 7<=convert(time)<= 8:
        print("breakfast time")
    elif 12 <=convert(time)<=13:
        print("lunch time")
    elif 18 <= convert(time)<=19:
        print("dinner time")


def convert(time):
    hour,minute=time.split(":")
    minute=int(minute)/60
    return (int(hour)+minute)


if __name__ == "__main__":
    main()