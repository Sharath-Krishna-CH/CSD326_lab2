class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def display_table(self):
        for employee in self.employees:
            print(employee)

    def sort_table(self, key):
        self.employees.sort(key=lambda x: getattr(x, key.lower()))

    def sort_and_display(self, sort_option):
        if sort_option == 1:
            self.sort_table("age")
        elif sort_option == 2:
            self.sort_table("name")
        elif sort_option == 3:
            self.sort_table("salary")
        else:
            print("Invalid sorting option. Please choose 1, 2, or 3.")
            return

        print("\nSorted Employee Table:")
        self.display_table()

if __name__ == "__main__":
    employees_data = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000),
    ]

    employee_table = EmployeeTable(employees_data)

    print("Employee Table:")
    employee_table.display_table()

    sort_option = int(input("\nChoose sorting parameter (1. Age, 2. Name, 3. Salary): "))
    employee_table.sort_and_display(sort_option)
