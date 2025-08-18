from enum import Enum

# 1. Enumeration for Department
class Department(Enum):
    HR = "Human Resources"
    IT = "Information Technology"
    DATA_SCIENCE = "Data Science"
    FINANCE = "Finance"

# 2. Base Employee Class
class Employee:
    def __init__(self, name: str, emp_id: int, department: Department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    # Dunder methods
    def __str__(self):
        return f"{self.name} ({self.emp_id}) - {self.department.value}"

    def __repr__(self):
        return f"Employee('{self.name}', {self.emp_id}, {self.department})"

    def __eq__(self, other):
        return isinstance(other, Employee) and self.emp_id == other.emp_id

# 3. Manager Class
class Manager(Employee):
 
    def __init__(self, name: str, emp_id: int, department: Department, employees=None):
        super().__init__(name, emp_id, department)
        if employees is not None:
            self.employees = employees
        else:
            self.employees = []
            
    def addEmployees(self, emp):
        if isinstance(emp, list):
            for e in emp:
                if e not in self.employees:
                    self.employees.append(e)
        else:
            if emp not in self.employees:
                self.employees.append(emp)
 
    def removeEmployees(self, emp):
        if isinstance(emp, list):
            for e in emp:
                if e in self.employees:
                    self.employees.remove(e)
        else:
            if emp in self.employees:
                self.employees.remove(emp)
 
    def printEmployees(self):
        print(f"Employees under {self.name}:")
        for emp in self.employees:
            print('-->', emp.name)
            
            
#class Manager(Employee):
#    def __init__(self, name: str, emp_id: int, department: Department):
#        super().__init__(name, emp_id, department)
#        self.team = []
#
#    def add_to_team(self, employee: Employee):
#        if employee not in self.team:
#            self.team.append(employee)
#
#    def __str__(self):
#        return f"Manager: {super().__str__()} | Team size: {len(self.team)}"

# 4. Developer Class
class Developer(Employee):
    def __init__(self, name: str, emp_id: int, department: Department, programming_language: str):
        super().__init__(name, emp_id, department)
        self.programming_language = programming_language

    def __str__(self):
        return f"Developer: {super().__str__()} | Language: {self.programming_language}"

# 5. Specialized Classes
class HRManager(Manager):
    def __init__(self, name: str, emp_id: int):
        super().__init__(name, emp_id, Department.HR)

class PythonDeveloper(Developer):
    def __init__(self, name: str, emp_id: int):
        super().__init__(name, emp_id, Department.IT, "Python")

class DataScientist(Developer):
    def __init__(self, name: str, emp_id: int):
        super().__init__(name, emp_id, Department.DATA_SCIENCE, "Python & ML Tools")

# 6. Demonstration
if __name__ == "__main__":
    # Create Employees
    emp1 = Employee("Alice", 101, Department.FINANCE)
    emp2 = Employee("Bob", 102, Department.IT)
    print("--- Employee Instances ---")
    print(emp1)
    print(emp2)
    print("emp1 __repr__:", repr(emp1))
    print("emp1 == emp2:", emp1 == emp2)
    print("emp1 == Employee('Another Alice', 101, Department.FINANCE):", emp1 == Employee("Another Alice", 101, Department.FINANCE))

    # Create Developers
    dev1 = PythonDeveloper("Charlie", 103)
    dev2 = DataScientist("David", 104)
    print("\n--- Developer Instances ---")
    print(dev1)
    print(dev2)
    print("dev1 __repr__:", repr(dev1))
    print("dev2 __repr__:", repr(dev2))

    # Create Manager
    mgr = HRManager("Eve", 201)
    print("\n--- HRManager Instance ---")
    print(mgr)
    print("Adding employees to manager...")
    mgr.addEmployees(emp1)
    mgr.addEmployees([dev1, dev2])
    mgr.printEmployees()

    print("\nRemoving an employee from manager...")
    mgr.removeEmployees(dev1)
    mgr.printEmployees()

    # Show Manager's __str__ and __repr__
    print("mgr __repr__:", repr(mgr))

    # Show inheritance and isinstance
    print("\n--- Inheritance and isinstance checks ---")
    print("Is mgr an instance of Employee?", isinstance(mgr, Employee))
    print("Is dev2 an instance of Developer?", isinstance(dev2, Developer))
    print("Is dev2 an instance of Employee?", isinstance(dev2, Employee))

    # Show department Enum usage
    print("\n--- Department Enum Usage ---")
    for dept in Department:
        print(dept, ":", dept.value)

    # Show custom attributes
    print("\n--- Custom Attributes ---")
    print(f"{dev1.name}'s programming language:", dev1.programming_language)
    print(f"{dev2.name}'s programming language:", dev2.programming_language)

    # Add and remove multiple employees
    print("\n--- Add/Remove Multiple Employees ---")
    mgr.addEmployees([emp2, dev1])
    mgr.printEmployees()
    mgr.removeEmployees([emp1, dev2])
    mgr.printEmployees()
