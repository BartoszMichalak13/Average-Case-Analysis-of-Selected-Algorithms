import numpy as np
import random

'''Generuje prosty graf pełny o n wierzchołkach, z wagami krawędzi
pochodzącymi z rozkładu dist z parametrami *params.
Dostępne rozkłady: 
'uniform'       -       rozkład jednostajny;        *params: a, b - krańce przedziału
'beta'          -       rozkład beta;               *params: alpha, beta
'gamma'         -       rozkład gamma;              *params: alpha, beta
Zwraca macierz sąsiedztwa grafu z jego wagami.'''
def graph_rand_weights(n, dist, *params):
    graph = np.zeros((n, n), dtype=np.float64)
    for i in range(n):
        for j in range(i + 1, n):
            if dist == 'uniform':
                w = random.uniform(*params)
            elif dist == 'beta':
                w = random.betavariate(*params)
            elif dist == 'gamma':
                w = random.gammavariate(*params)
            else:
                raise ValueError('Unrecognized distribution')
            graph[i,j] = graph[j,i] = w
    return graph


# print(graph_rand_weights(5, 'uniform', 0, 1))
# graph_rand_weights(5000, 'beta', 0.5, 0.5)
