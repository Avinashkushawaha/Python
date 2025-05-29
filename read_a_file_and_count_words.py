def word_count(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return len(text.split())