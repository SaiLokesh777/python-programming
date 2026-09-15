name= input("enter student name : ")
list=[]
for i in range(1,6):
    marks=(int(input(f"enter {i} subjects marks :")))
    list.append(marks)
print(list)

# def calculate():
#     return totalmarks,avgmarks,highestmarks,lowestmarks
# total marks
sum=0
for j in list:
    sum=sum+j
print("total marks out of 500  :",sum)   

# average marks
avg=sum/5
print("average marks :",avg)

# highest marks
highest=max(list)
print("highest marks :",highest)



# lowest marks
lowest=min(list)
print("lowest marks :",lowest)

# grading system

def  grade(avg):
    if avg>=90:
        print("grade : A")
    elif avg>=80:
        print("grade : B")
    elif avg>=70:
        print("grade : C")
    elif avg>=60:
        print("grade : D")
    else:
        print("grade : F")

print(grade(avg))

# store the data in a text file
with open("student.txt","w")as file:
    file.write(f"student name :{name}\n")
    file.write(f"marks of 5 subjects :{list}\n")
    file.write(f"total marks out of 500 :{sum}\n")
    file.write(f"average marks :{avg}\n")
    file.write(f"highest marks :{highest}\n")
    file.write(f"lowest marks :{lowest}\n")
    file.write(f"grade :{grade(avg)}\n")

# read the stored file
with open("student.txt","r")as file:
    content=file.read()
    print(content)



