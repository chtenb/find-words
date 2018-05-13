import sys
from search import is_word_in_graph
from wordgrid import WordSearchGrid


def chunker(seq, size):
    return [seq[pos:pos + size] for pos in range(0, len(seq), size)]

rowsize =  int(sys.argv[1])
inputstring = sys.argv[2]
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
