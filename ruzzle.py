import sys
from search import is_word_in_graph
from wordgrid import WordSearchGrid


def chunker(seq, size):
    return [seq[pos:pos + size] for pos in range(0, len(seq), size)]

rowsize =  4
language = sys.argv[1]
inputstring = sys.argv[2]
grid = WordSearchGrid([list(row) for row in chunker(inputstring, rowsize)])

if language == 'dutch':
    scoremap = dict(zip('qwertyuiopasdfghjklzxcvbnm', [int(i) for i in '95122822141224344335854413']))
    wordfilename = './dutch-words/words.txt'
elif language == 'english':
    scoremap = dict(zip('qwertyuiopasdfghjklzxcvbnm', [int(i) for i in '94111411131124248519834313']))
    wordfilename = './english-words/words.txt'
elif language == 'swedish':
    scoremap = dict(zip('abcdefghijklmnoprstuvxyzäåö', [int(i) for i in '148113221721212411143879344']))
    wordfilename = './swedish-words/Swedish.dic.txt'


found_words = []
with open(wordfilename) as f:
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
    print(word)
