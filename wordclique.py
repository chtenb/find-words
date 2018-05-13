

from graph import Graph
from bitset import iterate, size, contains, bit, bits, disjoint, index, domain, tolist


class WordSearchClique(Graph):

    """Graph of letters like in puzzles like ruzzle."""

    def __init__(self, letters: list):
        """
        :letters: list of of letters.
        """
        self.letters = letters

        neighborhoods = {}
        vertices = 0
        self.vertices_to_letters = {}
        self.letters_to_vertices = {}

        vertex = 0
        nr_letters = len(letters)
        all_vertices = (1 << nr_letters) - 1
        for i, letter in enumerate(letters):
            vertex = 1 << i
            neighbors = all_vertices

            self.vertices_to_letters[vertex] = letter.upper()
            if letter not in self.letters_to_vertices:
                self.letters_to_vertices[letter] = 0
            self.letters_to_vertices[letter] |= vertex

            neighborhoods[vertex] = neighbors

        Graph.__init__(self, all_vertices, neighborhoods)

    @staticmethod
    def from_string(s):
        """
        The string s is a string of letters separated by newlines, which indicate the
        end of a row.
        """
        return WordSearchGrid(list(s))


