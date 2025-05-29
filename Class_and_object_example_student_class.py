class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        return f"Name: {self.name}, Roll: {self.roll}"

s = Student("Avinash", 101)
print(s.display())