import sys
from search import is_word_in_graph
from wordgrid import WordSearchGrid

from common import unix_stdout, inputstring, scoremap, wordfilename

def chunker(seq, size):
    return [seq[pos:pos + size] for pos in range(0, len(seq), size)]

rowsize =  4
grid = WordSearchGrid([list(row) for row in chunker(inputstring, rowsize)])

found_words = []
with open(wordfilename, encoding='utf-8') as f:
    words = f.readlines()
    for word in words:
        # Strip \n and make lower
        word = word.lower()[:-1]
        if is_word_in_graph(word, grid):
            found_words.append(word)

def word_score(word):
    try:
        return sum(scoremap[letter] for letter in word)
    except KeyError:
        return 0

found_words.sort(key=lambda s: word_score(s))
for word in found_words:
    print(word, file=unix_stdout)
