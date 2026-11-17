employee_database = []

def add_employee(employee_name, employee_id, salary):
    """
    Adds a new employee to the employee database.

    Parameters:
    employee_name (str): The name of the employee.
    employee_id (int): The unique ID of the employee.
    salary (float): The salary of the employee.

    Returns:
    dict: A dictionary containing the employee's information.
    """
    employee = {
        'name': employee_name,
        'id': employee_id,
        'salary': salary
    }

    with open('employees.txt', 'a') as file:
        file.write(f"{employee_name} | {employee_id} | {salary}\n")
    # Here you would typically add the employee to a database or a list
    print(f"Employee {employee_name} added successfully!")

def view_employees():
    """
    Displays the list of employees in the employee database.
    """
    with open('employees.txt', 'r') as file:
        employees = file.readlines()

    return employees

while True:
    print("Employee Salary Management System")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter employee name: ")
        emp_id = int(input("Enter employee ID: "))
        salary = float(input("Enter employee salary: "))
        new_employee = add_employee(name, emp_id, salary)
    elif choice == '2':
        employees = view_employees()
        if not employees:
            print("No employees found.")
            continue
        else:
            employee_list = [emp.strip().split('|') for emp in employees]
            print("Employee List:")
            for emp in employee_list:
                print(f"Name: {emp[0]}, ID: {emp[1]}, Salary: {emp[2]}")
    elif choice == '3':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")
