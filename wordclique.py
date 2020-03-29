# Enable importing modules from graph-problems folder
import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, current_dir + '/graph-problems')


from graph import Graph
from bitset import iterate, size, contains, bit, bits, disjoint, index, domain, tolist
from collections import defaultdict


class WordSearchClique(Graph):

    def __init__(self, letters: list):
        """
        :letters: list of of letters.
        """
        letters = [l.lower() for l in letters]
        self.letters = letters

        neighborhoods = {}
        vertices = 0
        self.vertices_to_letters = defaultdict(lambda: 0)
        self.letters_to_vertices = defaultdict(lambda: 0)

        vertex = 0
        nr_letters = len(letters)
        all_vertices = (1 << nr_letters) - 1
        for i, letter in enumerate(letters):
            vertex = 1 << i
            neighbors = all_vertices

            self.vertices_to_letters[vertex] = letter
            if letter not in self.letters_to_vertices:
                self.letters_to_vertices[letter] = 0
            self.letters_to_vertices[letter] |= vertex

            neighborhoods[vertex] = neighbors

        Graph.__init__(self, all_vertices, neighborhoods)

    @staticmethod
    def from_string(s):
        return WordSearchClique(list(s))


