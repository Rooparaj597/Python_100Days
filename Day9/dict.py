#dictionary is denoted as {}
#each element in a dictionary has its key and its value
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# to print the specific value in dictionary use its key in a []

print(programming_dictionary["Bug"])

# you can also add new element in that existing dictionary
programming_dictionary["one"] = 1

# also wipe an entire dictionary by using empty {}
# programming_dictionary = {}

#loop through the entire dictionary by using for loop

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])



