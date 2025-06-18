def coroutine_example():
    print("Coroutine ready!")
    while True:
        val = yield 
        print(f"Received value: {val}")

co = coroutine_example()
next(co)  
co.send("Hello")  
    