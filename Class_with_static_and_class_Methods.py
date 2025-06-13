class Employee:
    company = "TechCorp"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_adult(age):
        return age >= 18 
    
    classmethod
    def company_name(cls):
        return cls.company
    
e = Employee("Alice")
print(Employee.is_adult(22))
print(Employee.company_name())    
        