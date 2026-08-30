# Print all prime numbers up to a given number


# n=int(input("enter start number up to print:"))
# m=int(input("enter end number up to print:"))
# for i in range(n,m+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count == 2:     
#         print(i)


# type 1

# n=int(input("enter a number:"))

# count=0
# for i in  range(2,n+1):
#     if n%i==0:
#         count +=1

# if count==1:
#     print("prime")
# else:
#     print("not prime")

# type 2

n=int(input("enter a number:"))

count=0
for i in  range(2,n+1):
    if n%i==0 :
        count +=1

if count==1:
    print("prime")
else:
    print("not prime")

# type 3

# n=int(input("enter start number up to print:"))
# m=int(input("enter end number up to print:"))
# for i in range(n,m+1):
#     fact=0
#     for j in range(1,(i//2)+1):
#         if i%j==0:
#             fact+=1
#     if fact == 1:     
#         print(i)
    
