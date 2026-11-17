basic_salary = float(input("Enter Basic Salary: "))

hra = basic_salary * 20 / 100
da = basic_salary * 10 / 100

gross_salary = basic_salary + hra + da

print("\nEmployee Salary Details")
print("-----------------------")
print("Basic Salary:", basic_salary)
print("HRA (20%):", hra)
print("DA (10%):", da)
print("Gross Salary:", gross_salary)
