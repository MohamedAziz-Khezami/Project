ph=input("Give your variable name: ")
ph2=""
for i in ph:

    if i.isupper():
        ph2+="_"
        i=i.lower()
    ph2+=i

print(ph2)
