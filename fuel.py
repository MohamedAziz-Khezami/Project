def fraction():
    while True:
        try:
            ph=input("Fraction: ")
            d,b=ph.split("/")
            x=(int(d)/int(b))

            if x>1:
                continue

            else:
                if 0<=x*100<=1:
                    print("E")

                elif 99<=x*100<=100:
                    print("F")

                else:

                    print(int(round(x*100)),"%",sep="")

            break

        except (ValueError, ZeroDivisionError):
            pass

def main():
    fraction()

if __name__=='__main__':
    main()