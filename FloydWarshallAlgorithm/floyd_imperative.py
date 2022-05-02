"""
An alternative python program to the main module for Floyd Warshall Algorithm using imperative. 
"""
import sys, itertools

NO_PATH = sys.maxsize

graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
    ]

N = len(graph[0])

def floyd(distance):
    """
    A simple implementation of Floyd's algorithm
    """
    for intermediate, start_node,end_node\
                        in itertools.product\
                        (range(N),range(N), range(N)):
    
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        #return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],
                        distance[start_node][intermediate] + distance[intermediate][end_node] )

    #Any value that have sys.maxsize has no path
    print (distance)
   
floyd(graph)