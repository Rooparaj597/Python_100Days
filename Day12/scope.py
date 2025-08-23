enemies = 1
#its a global variable, its used inside the function and also outside the function

def increase_enemies():
    enemies_2 = 2
    #its a local variable it only used inside the function
    print(f"enemies inside function: {enemies_2}")

# cant able to use the local variable outside the function
# print(enemies_2)
increase_enemies()
print(f"enemies outside function: {enemies}")
