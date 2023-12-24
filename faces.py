def convert(to):
    return to.replace(":)","🙂").replace(":(","🙁")


def main():
    ph=input('Give your phrase: ')
    print(convert(ph))


main()