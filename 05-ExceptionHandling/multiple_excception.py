a=int(input("enter a  number:"))
b=int(input("enter a  number:"))

try:
    print(a/b)
except ValueError:
    print("pls enter number only")
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print("division successful")
