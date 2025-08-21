import random

#random.ranint(a, b) is used to print the random value between a and b

Toss = random.randint(0, 1)

if Toss==0:
    print("Heads")
else:
    print("Tails")
