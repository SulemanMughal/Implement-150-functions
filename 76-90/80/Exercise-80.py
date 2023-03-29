def top_n(items, n):
    items.sort(reverse=True)
    return items[:n]