import random

highest = 10
answer = random.randint(1, highest)
guess = 0   # initialize to any number that doesn't equal the answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be greater than answer
            print("Please guess lower")
