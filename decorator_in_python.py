def greet(fx):
   def mfx(*args, **kwargs):
    print("Good Morning")
    fx()
    print("Thanks for using this function")
   return mfx 


@greet
def hello():
    print("Hello world")

def add(a, b):
   print(a+b)    

hello()
