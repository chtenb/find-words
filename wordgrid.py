

from graph import Graph
from bitset import iterate, size, contains, bit, bits, disjoint, index, domain, tolist


class WordGrid(Graph):

    """Graph of letters like in puzzles like ruzzle."""

    def __init__(self, grid):
        """
        :grid: grid of of letters as a 2D list.
        """
        self.grid = grid

        neighborhoods = {}
        vertices = 0
        vertices_to_letters = {}

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
                        result |= cell_to_vertex(i, j)
            return result

        vertex = 0
        for row in range(height):
            for col in range(width):
                vertex = cell_to_vertex(row, col)
                neighbors = get_neighbors(row, col)
                vertices_to_letters[vertex] = grid[row][col]
                vertices |= vertex
                neighborhoods[vertex] = neighbors

        Graph.__init__(self, vertices, neighborhoods)


