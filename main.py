# Enable importing modules from graph-problems folder
import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, current_dir + '/graph-problems')

from wordgrid import WordGrid

grid = WordGrid(
    [
        ['a','b','c'],
        ['d','e','f'],
        ['g','h','i'],
    ]
)

from plot import plot

plot(grid)

