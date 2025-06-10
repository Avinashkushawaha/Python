class Employee:
    company = "OpenAI"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_adult(age):
        return age >= 18

    @classmethod
    def company_name(cls):
        return cls.company

e = Employee("Avinash")
print(Employee.is_adult(22))     # True
print(Employee.company_name())   # OpenAI
