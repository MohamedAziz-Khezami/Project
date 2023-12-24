def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    abc=0
    p=""
    for i in range(len(s)):
        if s[i].isalpha():
            abc+=1
        elif s[i].isdigit():
            p+=s[i:]
            break

    return 0<len(s)<=6 and abc>=2 and ((p.isdigit() and p[0]!="0") or p=="")



main()