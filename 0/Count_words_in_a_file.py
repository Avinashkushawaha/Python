def count_words(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return len(text.split())

# Save this as a file and use: print(count_words("yourfile.txt"))
