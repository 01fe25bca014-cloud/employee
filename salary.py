basic_salary = 50000

hra = basic_salary * 20 / 100
da = basic_salary * 10 / 100

gross_salary = basic_salary + hra + da

print("Employee Salary Details")
print("Basic Salary:", basic_salary)
print("HRA (20%):", hra)
print("DA (10%):", da)
print("Gross Salary:", gross_salary)