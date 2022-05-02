"""
Two performances test are compared for the FLoyd Warshall Algorithm
comparing recursive with imperative approach.
"""

import timeit

# Comparing the two execution times
exec_time1 = timeit.timeit(setup = 'from floyd_imperative import floyd, graph', 
                           stmt = 'floyd(graph)', 
                           number = 10)

exec_time2 = timeit.timeit(setup = 'from main import floyd_rec, graph', 
                           stmt = 'floyd_rec(graph)', 
                           number = 10)

print("Imperative execution time:", exec_time1)
print("Recursive execution time:", exec_time2)
