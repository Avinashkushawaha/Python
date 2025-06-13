import time 

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Time taken:", time.time() - start, "sconds")
        return result 
    
@timer 
def slow_function():
    time.sleep(1)
    return "Done!"

print(slow_function())
