class Person:
   def __init__(self, n, o):
    print('Hey I am person')
    self.name = n
    self.occ = o

    def info(self):
      print(f"{self.name} is a {self.occ}")


a = Person('harry', 'developer')
b = Person('divya', 'hr')
c = Person()
a.info()
b.info()
