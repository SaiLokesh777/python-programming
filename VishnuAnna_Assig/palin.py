num=input("Enter: ")
# print(num[: :-1])
end=len(num)-1
for i in range(len(num)):
    if num[i]==num[end-i]:
        print(" palin")  
        break     
else:
    print("not palin")
