# Enable importing modules from graph-problems folder
import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, current_dir + '/graph-problems')

from bitset import iterate, subtract



def recurse(word: str, graph, last_vertex, forbidden):
    if not word:
        return True

    letter = word[0]

    if letter not in graph.letters_to_vertices:
        return False

    candidates = subtract(graph.letters_to_vertices[letter] &
                          graph.neighborhoods[last_vertex], forbidden)
    if not candidates:
        return False

    return any(recurse(word[1:], graph, v, forbidden | v) for v in iterate(candidates))


def is_word_in_graph(word: str, graph):
    if not word:
        return False

    letter = word[0]
    candidates = (graph.letters_to_vertices[letter]
                  if letter in graph.letters_to_vertices else 0)
    if not candidates:
        return False

    return any(recurse(word[1:], graph, v, v) for v in iterate(candidates))

