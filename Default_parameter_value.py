# write a function that greets a user.if no name is provided, it should greet with a default name.
def greet(name = 'User'):
    return "hello," + name + " !"

print(greet())