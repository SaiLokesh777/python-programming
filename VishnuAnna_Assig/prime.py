p=int(input("enter start number:"))
q=int(input("enter end number:"))
primecount=0
for i in range(p,q+1):
    count=0
    for j in range(2,i-1):
        if i%j ==0:
            count +=1
    if count==0:
        print(i,"prime")
        primecount +=1
    else:
        print(i,"not prime")
print(f"primes:{primecount}")
notprimes=q-primecount
print(f"not primes:{notprimes}")

