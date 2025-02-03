class Employee:
    def __init__(self, name):
        self.name = name
    def showDetails(self):
        print(f"The name of the Employee is {self.name}") 

emp1 = Employee("Harry")
Employee.showDetails(emp1)        
