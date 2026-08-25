n=int(input("enter number:"))
count=0
for i in range(0,n+1,2):
    count +=1
    print(i)
print("count of even numbers:", count)