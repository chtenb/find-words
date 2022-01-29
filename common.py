import sys

unix_stdout = open(sys.__stdout__.fileno(),
                   mode=sys.__stdout__.mode,
                   buffering=1,
                   encoding=sys.__stdout__.encoding,
                   errors=sys.__stdout__.errors,
                   newline='\n',
                   closefd=False)

language = sys.argv[1]
inputstring = sys.argv[2]

if language == 'dutch':
    scoremap = dict(zip('qwertyuiopasdfghjklzxcvbnm', [int(i) for i in '95122822141224344335854413']))
    wordfilename = './dutch-words/all.txt'
elif language == 'english':
    scoremap = dict(zip('qwertyuiopasdfghjklzxcvbnm', [int(i) for i in '94111411131124248519834313']))
    wordfilename = './english-words/words.txt'
elif language == 'swedish':
    scoremap = dict(zip('abcdefghijklmnoprstuvxyzäåö', [int(i) for i in '148113221721212411143879344']))
    wordfilename = './swedish-words/Swedish.dic.txt'
