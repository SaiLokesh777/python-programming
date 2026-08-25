age = int(input("Enter your age: "))

print(
    "You have entered a wrong age. Please enter a valid age."
    if age < 0
    else "Eligible to vote"
    if age >= 18
    else "Not eligible to vote"
)