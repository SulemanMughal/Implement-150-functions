def convert(text):
    mapping = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        }
    words = text.split()
    digits = mapping.keys()
    for (idx, word) in enumerate(words):
        if word in digits:
            words[idx] = mapping[word]
    return ' '.join(words)