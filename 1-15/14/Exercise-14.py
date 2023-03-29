def top3(data):
    for idx, row in enumerate(data):
        row.sort(reverse=True)
        data[idx] = row[:3]
    return data