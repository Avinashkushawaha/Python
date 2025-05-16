class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of Employee is {self.name} and the salary is {self.company}")


class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the language here is language: {self.language} ")

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and the salary is {self.language}")

    # def showLanguage(self):
    #     print(f"THe name is {self.name} and he is good with {self.Language} language") 

a = Employee()
b = Programmer()


b.show()
b.printLanguages()
b.showLanguage()
# print(a.company, b.company)


