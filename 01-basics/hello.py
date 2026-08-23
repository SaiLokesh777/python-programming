# print("hi friends")

# friends=int(input("how many friends o  you hava"))
# print(f"ooo do you hava {friends} friends thats good")

# shop=input("whch shop did you went")
# print(f"{shop}  is very popular")
# item=input("what are the items did you buy")
# print(f"{item} these are so expensive")


"""type casting"""
# num="10"
# cgpa=3.0
# name="hello"
# is_it_rain=""

# print(int(cgpa))
# print(float(num))
# print(str(num))
# num +="1"
# print(num)
# print(bool(is_it_rain))

"""positive or negative"""
# num=int(input("enter a number"))
"""print("positive" if num>0 else "negative")  (choice)"""
# if num>=0:
#     print("positive")
# else:
#     print("negative")

"""divisible by 2"""
# n=int(input("enter an integer"))

# print("divisible by 2" if n%2==0 else"not divisible")

"""eligible to vote"""
# age = int(input("Enter your age: "))

# print(
#     "You have entered a wrong age. Please enter a valid age."
#     if age < 0
#     else "Eligible to vote"
#     if age >= 18
#     else "Not eligible to vote"
# )

"""valid user input exercise"""
# name=str(input("enter user name"))
# if len(name)<=12 and " " not in name and  not name.isdigit :
#     print("user name is valid")
# else:
#     print(f"user entered is{name} this is not valid")

"""  format specifears """

# num1=20937.9
# num2=-0.9876
# num3=57647.0

# print(f"num 1 entered number id {num1:.10f}")
# print(f"you entered number is {num2:.3f}")
# print(f"you have enteered number is {num3 : .10f}")

""" string slicing"""

# jack="lokesh287sai"

# print(jack[::-1])
# print(jack[0:4])
# print(jack[3::2])
# print(jack[2:7])

"""while loop"""

# name=str(input("enter name :"))
# # name=""
# while name=="":
#     name=str(input("enter name :"))
#     print("name shoild be not empty")
    
# print(f"entered name is :{name}")

"""for loop"""

# # x=23445
# for  x in range(0,10,2 ):
#     print(x)

# n="saiki"
# for x in range(1,3):
#     print(n[x])

# n="saiki"
# for x in range(4):
#     print(n[x])

# """break ,continue"""

# for i in range(1,20):
#     if i==7:
#         continue
# print(i)

"""break ,continue"""

for i in range(1,20):
    print(i,"even" if i%2==0 else" odd")
    
    