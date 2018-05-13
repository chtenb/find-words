import sys
from pyshellout import *

from search import is_word_in_graph
from wordclique import WordSearchClique

inputstring = sys.argv[1]
graph = WordSearchClique.from_string(inputstring)

found_words = []
with open('./dutch-words/nederlands.txt') as f:
    words = f.readlines()
    for word in words:
        # Strip \n and make upper
        word = word.upper()[:-1]
        if is_word_in_graph(word, graph):
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
