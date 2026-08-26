# Print all prime numbers up to a given number

n=int(input("enter number up to print:"))

for i in range(1,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count +=1
    if count ==2:     
        print(i)

    
