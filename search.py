# Enable importing modules from graph-problems folder
import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, current_dir + '/graph-problems')

from bitset import iterate, subtract


def is_word_in_graph(word: str, graph, last_vertex=0, forbidden_vertices=0):
    if not word:
        return True

    letter = word[0]
    candidates = graph.letters_to_vertices[letter] | graph.letters_to_vertices['.']
    candidates = subtract(candidates, forbidden_vertices)
    if last_vertex:
        candidates &= graph.neighborhoods[last_vertex]

    return any(is_word_in_graph(word[1:], graph, v, forbidden_vertices | v) for v in iterate(candidates))

