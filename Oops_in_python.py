class Person:
    name = 'Harry'
    occupation = 'Software Developer'
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
# a.name = 'shubham'
# a.occupation = 'avi'
print(a.name, a.occupation)   
