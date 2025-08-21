import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]


# use random.randint() to generate random number

random_name= random.randint(0,4)

#now put that random no in the index position to get random name

print(friends[random_name])