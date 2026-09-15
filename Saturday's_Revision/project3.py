# Employee Salary Analyzer

employees = {
    "Lokesh": 30000,
    "Rahul": 45000,
    "sai": 25000,
    "ravi": 50000,
    "kumar": 40000,
    "ravi": 35000
}

for name,salary in employees.items():
    print(f"Employee: {name}, Salary: {salary}")

# highest salary
highest_salary = max(employees.values())
print(f"Highest Salary: {highest_salary}")
# lowest salary
lowest_salary = min(employees.values())
print(f"Lowest Salary: {lowest_salary}")

# average salary
average_salary = sum(employees.values()) / len(employees)
print(f"Average Salary: {average_salary}")

for name, salary in employees.items():
    if salary > 30000:
        print(f"{name} has a salary greater than 30000")

# unique salaries
unique_salaries = set(employees.values())
print(f"Unique Salaries: {unique_salaries}")

for name, salary in employees.items():
    if salary >= 50000:
        category = "High"
    elif salary >= 30000:
        category = "Medium"
    else:
        category = "Low"

    print(name, category)