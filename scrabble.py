import sys
from pyshellout import *

from search import is_word_in_graph
from wordclique import WordSearchClique

# dictionary = './dutch-words/nederlands.txt'
dictionary = './dutch-words/Dutch.txt'

try:
    inputstring = sys.argv[1]
except IndexError:
    inputstring = None
else:
    graph = WordSearchClique.from_string(inputstring)

found_words = []
with open(dictionary) as f:
    words = f.readlines()
    if inputstring == None:
        for word in words:
            print(word)
        sys.exit()
    for word in words:
        # Strip \n and make lower
        word = word.lower()[:-1]
        if is_word_in_graph(word, graph):
            found_words.append(word)

scoremap = dict(zip('abcdefghijklmnopqrstuvwxyz', [int(i) for i in '14521434243331149222245885']))
def word_score(word):
    '''Assuming dutch wordfeud score'''
    try:
        return sum(scoremap[letter] for letter in word)
    except KeyError:
        return 0

found_words.sort(key=lambda s: word_score(s))
for word in found_words:
    print(word)
