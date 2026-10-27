import sys
def employee_details(name,employee_id,department,salary):
    return f"Name: {name}\nEmployee ID:{employee_id}\nDepartment:{department}\nSalary:{salary}"
if __name__ == "__main__":
    name =sys.argv[0]
    employee_id = sys.argv[1]
    department =sys.argv[2]
    salary =sys.argv[3]

    print("\nEmployee Details")
    print("-----------------")
    print(employee_details(name,employee_id,department,salary))