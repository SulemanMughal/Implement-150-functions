# Solution 1

from collections import ChainMap
    
    
english_scoreboard = {
    ' ': 0,
    'EAIONRTLSU': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10
}
    
    
def score(word):
    scores = ChainMap(*[dict.fromkeys(letter, score)
                        for letter, score in english_scoreboard.items()])
    return sum([scores[letter.upper()] for letter in word])


letters = {
    ' ': 0,
    'E': 1,
    'A': 1,
    'I': 1,
    'O': 1,
    'N': 1,
    'R': 1,
    'T': 1,
    'L': 1,
    'S': 1,
    'U': 1,
    'D': 2,
    'G': 2,
    'B': 3,
    'C': 3,
    'M': 3,
    'P': 3,
    'F': 4,
    'H': 4,
    'V': 4,
    'W': 4,
    'Y': 4,
    'K': 5,
    'J': 8,
    'X': 8,
    'Q': 10,
    'Z': 10
}
    
    
def score(word):
    return sum([letters[letter.upper()] for letter in word])