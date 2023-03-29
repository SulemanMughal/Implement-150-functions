def map_longest(words):
    length = []
    for word in words:
        length.append(len(word))
    return max(length)