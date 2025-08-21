# return in function will stop the remaining lines of code in the function
def format_name(f_name, l_name):

    if f_name == "" or l_name == "":
        # if the parameters are empty this will return the below string and stop the fuction
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name?"), input("What is your last name?")))
