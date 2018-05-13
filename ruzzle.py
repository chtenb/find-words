# Enable importing modules from graph-problems folder
import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, current_dir + '/graph-problems')

from wordgrid import WordSearchGrid
from bitset import iterate, subtract
from search import is_word_in_graph


rowsize =  int(sys.argv[1])
inputstring = sys.argv[2]

def chunker(seq, size):
    return [seq[pos:pos + size] for pos in range(0, len(seq), size)]

grid = WordSearchGrid([list(row) for row in chunker(inputstring, rowsize)])


found_words = []

# with open('./google-10000-english/google-10000-english.txt') as f:
# with open('./english-words/words.txt') as f:
with open('./dutch-words/nederlands.txt') as f:
    words = f.readlines()
    for word in words:
        # Strip \n and make upper
        word = word.upper()[:-1]
        if is_word_in_graph(word, grid):
            found_words.append(word)

scoremap = dict(zip('QWERTYUIOPASDFGHJKLZXCVBNM', [int(i) for i in '95122822141224344335854413']))
def word_score(word):
    '''Assuming dutch ruzzle score'''
    try:
        return sum(scoremap[letter] for letter in word)
    except KeyError:
        return 0

found_words.sort(key=lambda s: word_score(s))
for word in found_words:
    print(word)
