def count_none(items):
    counter = 0
    for item in items:
        if not item:
            counter += 1
    return counter