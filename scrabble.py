import sys
from pyshellout import *

from search import is_word_in_graph
from wordclique import WordSearchClique

language = sys.argv[1]
inputstring = sys.argv[2]

if language == 'dutch':
    scoremap = dict(zip('qwertyuiopasdfghjklzxcvbnm', [int(i) for i in '95122822141224344335854413']))
    wordfilename = './dutch-words/words.txt'
elif language == 'english':
    scoremap = dict(zip('qwertyuiopasdfghjklzxcvbnm', [int(i) for i in '94111411131124248519834313']))
    wordfilename = './english-words/words.txt'
elif language == 'swedish':
    scoremap = dict(zip('abcdefghijklmnoprstuvxyzäåö', [int(i) for i in '148113221721212411143879344']))
    wordfilename = './swedish-words/Swedish.dic.txt'

graph = WordSearchClique.from_string(inputstring)

found_words = []
with open(wordfilename, encoding='utf-8') as f:
    words = f.readlines()
    if inputstring == None:
        for word in words:
            print(word.lower()[:-1])
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
