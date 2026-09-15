with open("newdata.txt","w")as file:
    file.write("new file\n")

with open("newdata.txt","a")as file:
    file.write("Appending data into file\n")

with open("newdata.txt","r")as file:
    content=file.read()
print(content)