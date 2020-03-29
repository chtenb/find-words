# Enable importing modules from graph-problems folder
import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, current_dir + '/graph-problems')


from graph import Graph
from bitset import iterate, size, contains, bit, bits, disjoint, index, domain, tolist
from collections import defaultdict


class WordSearchGrid(Graph):

    """Graph of letters like in puzzles like ruzzle."""

    def __init__(self, grid):
        """
        :grid: grid of of letters as a 2D list.
        """
        self.grid = grid

        neighborhoods = {}
        vertices = 0
        self.vertices_to_letters = defaultdict(lambda: 0)
        self.letters_to_vertices = defaultdict(lambda: 0)

        width = len(grid[0])
        height = len(grid)

        def cell_to_vertex(row, col):
            """Return vertex corresponding to row and col. Return 0 if out of range."""
            if 0 <= row < height and 0 <= col < width:
                return 1 << row * width + col
            else:
                return 0

        def get_neighbors(row, col):
            """Return the set of neighbors corresponding to row and col."""
            result = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if not 0 == i == j:
                        result |= cell_to_vertex(row + i, col + j)
            return result

        vertex = 0
        for row in range(height):
            for col in range(width):
                vertex = cell_to_vertex(row, col)
                neighbors = get_neighbors(row, col)

                letter = grid[row][col].lower()

                self.vertices_to_letters[vertex] = letter
                if letter not in self.letters_to_vertices:
                    self.letters_to_vertices[letter] = 0
                self.letters_to_vertices[letter] |= vertex

                vertices |= vertex
                neighborhoods[vertex] = neighbors
                grid[row][col] = (vertex, self.vertices_to_letters[vertex])

        Graph.__init__(self, vertices, neighborhoods)

    @staticmethod
    def from_string(s):
        """
        The string s is a string of letters separated by newlines, which indicate the
        end of a row.
        """
        grid = [list(row) for row in s.split('\n') if row]
        return WordSearchGrid(grid)


