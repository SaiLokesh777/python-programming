n=int(input("Enter a number: "))
a=0
b=1

for i in range(n):
    res=a+b
    print(res)
    a=b
    b=res

