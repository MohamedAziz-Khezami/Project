
def pop(p):
    vowels=['a','e','i','o','u']
    h=""
    for i in p:
        if i.lower() in vowels:
            None
        else:
            h+=i
    return h



ph=input("input: ")

print("Output:",pop(ph))