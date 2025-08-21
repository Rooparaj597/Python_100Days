#default function

def greet():
    print("Hello")
    print("How are you!")
    print("Bye")

greet()

# Functions with input

def greet_byname(name):
    print(f"Hello {name}")
    print(f"How are you!")
    print((f"Bye {name}"))

greet_byname("Roopa")