def filter_ge_6(words):
    result = []
    for word in words:
        if len(word) >= 6:
            result.append(word)
    return result