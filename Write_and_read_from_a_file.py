def write_and_read():
    with open("test.txt", "w") as file:
        file.write("Hello Avinash!\nWelcome to Python.")

    with open("test.txt", "r") as file:
        content = file.read()
    return content

print(write_and_read())