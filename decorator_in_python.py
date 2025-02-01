def greet(fx):
   def mfx():
    print("Hello world")
    fx()
    print("Thanks for using this")
   return mfx 


@greet
def hello():
    print("Hello world")

def add(a, b):
   print(a+b)    

hello()
