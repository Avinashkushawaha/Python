class Person:
    name = 'Harry'
    occupation = 'Software Developer'
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
# a.name = 'shubham'
a.occupation = 'Accountant'
b.name = 'gitika'
b.occupation = 'manager'
# print(a.name, a.occupation)
b.info()
a.info()