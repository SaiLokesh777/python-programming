# a= int(input("enter a value:"))
# b=int(input("enter b value:"))

# def cal(a,b):
#     return a+b,a-b,a*b,a%b,a//b,a/b,a**b

# result=cal(a,b)

# print(result)

# num=input().lower()
# count=0
# for ch in  num:
#     if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
#        count +=1
# print(count)

num = input()

count = 0

for ch in num:
    if ch in "aeiouAEIOU":
        count += 1

print(count)