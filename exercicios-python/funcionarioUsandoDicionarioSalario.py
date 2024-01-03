dictionary = {}

while True:

    employee = input("Employee name: ")
    
    if employee == "end":
        break
    
    salary = float(input("And your salary: "))
   
    if employee not in dictionary:
        dictionary[employee] = salary
    
employeeBigger = max(dictionary, key=dictionary.get)
biggerSalary = dictionary[employeeBigger]

employeeSmaller = min(dictionary, key=dictionary.get)
smallerSalary = dictionary[employeeSmaller]

sum = 0

for i in dictionary.values():
    sum += i

average = sum / len(dictionary.values())

print(f'Bigger salary: {biggerSalary} (employee: {employeeBigger})')
print(f'Smaller salary: {smallerSalary} (employee: {employeeSmaller})')
print(f'Average salarial: {average}')
