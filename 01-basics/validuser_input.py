name=str(input("enter user name :"))
if len(name)<=12 and " " not in name and  not name.isdigit :
    print("user name is valid")
else:
    print(f"user entered is {name} this is not valid")
