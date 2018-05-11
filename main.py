# Enable importing modules from graph-problems folder
import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, current_dir + '/graph-problems')

from wordgrid import WordSearchGrid
from bitset import iterate, subtract


rowsize =  int(sys.argv[1])
inputstring = sys.argv[2]

def chunker(seq, size):
    return [seq[pos:pos + size] for pos in range(0, len(seq), size)]

grid = WordSearchGrid([list(row) for row in chunker(inputstring, rowsize)])


def recurse(word: str, graph: WordSearchGrid, last_vertex, forbidden):
    if not word:
        return True

    letter = word[0]

    if letter not in graph.letters_to_vertices:
        return False

    candidates = subtract(graph.letters_to_vertices[letter] &
                          graph.neighborhoods[last_vertex], forbidden)
    if not candidates:
        return False

    return any(recurse(word[1:], graph, v, forbidden | v) for v in iterate(candidates))


def is_word_in_graph(word: str, graph: WordSearchGrid):
    if not word:
        return False

    letter = word[0]
    candidates = (graph.letters_to_vertices[letter]
                  if letter in graph.letters_to_vertices else 0)
    if not candidates:
        return False

    return any(recurse(word[1:], graph, v, v) for v in iterate(candidates))


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
