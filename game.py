import random

while True:
    level = input("Level: ")
    if level.isdigit() and int(level)>=1:
        break
    else:
        continue

r = random.randint(1, int(level))
print(r)


while True:
    t = 1
    while t == 1:
        guess = input("Guess: ")
        if guess.isdigit():
            t += 1
        else:
            continue
    guess = int(guess)

    if guess == r:
        print("Just right!")
        break
    elif guess > r:
        print("Too large!")
        continue
    elif guess < r:
        print("Too small!")
        continue
