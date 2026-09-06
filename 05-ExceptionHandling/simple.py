# try:
#     a = 10
#     b = 0
#     print(a / b)
# except:
#     print("Something went wrong")



numbers = [10, 20, 30]

try:
    print(numbers[5])
except IndexError:
    print("Index does not exist")