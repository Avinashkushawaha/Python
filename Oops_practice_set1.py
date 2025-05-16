# Write a class calculator capable of finiding square cube and square root of a number

class Calcolator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square if {self.n*self.n}") 

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")


a = Calcolator(4)
a.square()
a.square()
a.square()