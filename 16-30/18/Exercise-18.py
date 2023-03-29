from itertools import permutations
    
    
def calculate(sentence):
    words = sentence.split()
    permutations_of_words = permutations(words)
    result = [' '.join(item) for item in permutations_of_words]
    return result   