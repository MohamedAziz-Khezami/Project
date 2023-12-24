due=50
coins=[5,10,25,50]
tt_coins=0

while True:
    print("Amount Due:",due)

    coin=int(input("Insert Coin: "))


    if coin in coins:
        tt_coins+=coin

        if tt_coins<50:
            due-=coin
        else:
            print("Change Owed:",tt_coins-50)
            break
    else:
        continue


