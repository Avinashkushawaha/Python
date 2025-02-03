class Employee:
    def __init__(self, name):
        self.name = name
    def showDetails(self):
        print(f"The name of the Employee is {self.name}") 

emp1 = Employee("Harry")
# Employee.showDetails(emp1)        
emp1.raise_amount = 0.3
emp1.showDetails()
emp2 = Employee("Rohan")
emp2.showDetails()