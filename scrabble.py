from pyshellout import *

from search import is_word_in_graph
from wordclique import WordSearchClique

from common import unix_stdout, inputstring, scoremap, wordfilename

graph = WordSearchClique.from_string(inputstring)

found_words = []
with open(wordfilename, encoding='utf-8') as f:
    words = f.readlines()
    for word in words:
        # Strip \n and make lower
        word = word.lower()[:-1]
        if inputstring == None or is_word_in_graph(word, graph):
            found_words.append(word)


def word_score(word):
    '''Assuming dutch wordfeud score'''
    try:
        return sum(scoremap[letter] for letter in word)
    except KeyError:
        return 0


found_words.sort(key=lambda s: word_score(s))
for word in found_words:
    print(word, file=unix_stdout)
