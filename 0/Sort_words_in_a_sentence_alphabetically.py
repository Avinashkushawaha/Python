def sort_words(sentence):
    return ' '.join(sorted(sentence.split(), key=str.lower))

print(sort_words("Python is a powerful and fast"))