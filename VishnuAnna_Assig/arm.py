n=int(input("Enter start number: "))
m=int(input("Enter end number: "))
sum=0
for ch in str(n):
    mul =int(ch)**3
    sum=sum+mul
    mul +=1
if sum==n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
