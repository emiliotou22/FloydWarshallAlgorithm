"""
Python Program for Floyd Warshall Algorithm using recursion with memoization. 
Floyd Warshall Algorithm returns the shortest path between any pair of nodes. 
"""

import sys, itertools
import numpy as np

# Assignes NO_PATH to the maximum size Python can receive
NO_PATH = sys.maxsize

graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
    ]

def floyd_rec(distance: list[list]) -> list[list]:
    """
    This function returns the shortest path between any pair of nodes in the given graph.
    The graph is given as a distance matrix. Replaces each item in the list with the shortest
    distance of the given nodes. 

    Parameters:
        distance (list[List]): a list of list of integers

    Returns:
        distance (list[List]): a list of list of integers with the shortest distance
    """
    N = len(distance[0])
    sp = np.inf*np.ones((N, N, N))

    def shortestPath(start_node: int, end_node: int, intermediate: int) -> float:
        """
        This function calcualtes the shortest path between two given nodes. 
        Memoization is used to imrpove recursion's performance

        Parameters:
            start_node (int): integer of the position of the start node
            end_node (int):  integer of the position of the end node
            intermediate (int):  integer of the position of the intermedia node

        Returns:
            sp: a list of list of integers with the shortest distance

        Keyword arguments:
            sp = shortest path matrix
        """
        if intermediate == 0:
            sp[start_node, end_node,0] = distance[start_node][end_node]
            return sp[start_node, end_node,0]
        
        # If the position is greater than positive infinity it indicates that it has 
        # been previously calculated and therefore there is no need to re-calculate  
        if sp[start_node, end_node, intermediate] < np.inf:
            return sp[start_node,end_node, intermediate]

        # First all possible paths are calculated between the start and end node,
        # and then the minimum of which is selected.
        sp[start_node, end_node, intermediate] = min(shortestPath(start_node, end_node, intermediate-1), 
                                                    shortestPath(start_node, intermediate, intermediate-1) 
                                                    + shortestPath(intermediate, end_node, intermediate-1))
        return sp[start_node, end_node, intermediate]
        
    for start_node,end_node\
                        in itertools.product\
                        (range(N), range(N)):
        
        distance[start_node][end_node] = int(shortestPath(start_node, end_node, N-1))

    return distance

print(floyd_rec(graph))