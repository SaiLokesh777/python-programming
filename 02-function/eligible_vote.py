def is_checkage(age):
    if age>18:
        return "eligible"
    else:
        return "not eligible"
    
age=int(input("enter age:"))
print(is_checkage(age))
    