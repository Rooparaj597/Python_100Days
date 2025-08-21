# Function gets input inside its parenthesis(in1, in2)

def full_name(f_name, l_name):
    formated_fname = f_name.title()
    formated_lname = l_name.title()

    print(formated_fname+" "+formated_lname)

full_name("RoOpa", "Raj")

# also give oen input in a function

def func1(text):
    return text + text

def func2(text):
    return text.title()
print(func2(func1("HelloOO")))