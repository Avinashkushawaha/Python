def flatten(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat

print(flatten([1, [2, [3, 4]], 5]))  # [1, 2, 3, 4, 5]
