def count_str(items):
    total = 0
    for item in items:
        if isinstance(item, str):
            if len(item) > 2:
                total += 1
    return total