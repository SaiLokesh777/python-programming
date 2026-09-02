try:
    user_input = int(input("enter a number:"))
    print("you entered integer :",user_input)
except ValueError:
    print("invalid input. please enter a valid integer.")