class Employee:
    companyName = "Apple"
    noOfEmployees = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployees += 1
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

emp1 = Employee("Harry")
# Employee.showDetails(emp1)        
emp1.raise_amount = 0.3
emp1.showDetails()
emp2 = Employee("Rohan")
emp2.showDetails()