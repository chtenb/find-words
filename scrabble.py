import sys
from pyshellout import *
_, minlength, maxlength, chars = sys.argv
cmd = "cat ./dutch-words/Dutch.txt | grep '^.\{{{},{}\}}$'" + " | grep {}"*len(chars)
args = [minlength, maxlength] + list(chars)
print(cmd.format(*args))
# out(cmd, *args, verbose=True)
