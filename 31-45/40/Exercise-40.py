def get_chunks(text, num):
    if len(text) <= num:
        return [text]
    return [text[:num]] + get_chunks(text[num:], num)