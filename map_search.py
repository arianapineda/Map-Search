"""
Map Search
"""

import comp140_module7 as maps
from collections import defaultdict
class Queue:
    """
    A simple implementation of a FIFO queue.
    """
    def __init__(self):
        """
        Initialize the queue.
        """
        self._queue = []

    def __len__(self):
        """
        Returns: an integer representing the number of items in the queue.
        """
        return len(self._queue)

    def __str__(self):
        """
        Returns: a string representation of the queue.
        """
        string = ""
        for val in self._queue:
            string += str(val) + " "
        return string

    def push(self, item):
        """
        Add item to the queue.

        input:
            - item: any data type that's valid in a list
        """
        self._queue.append(item)

    def pop(self):
        """
        Remove the least recently added item.

        Assumes that there is at least one element in the queue.  It
        is an error if there is not.  You do not need to check for
        this condition.

        Returns: the least recently added item.
        """
        
        return self._queue.pop(0)

    def clear(self):
        """
        Remove all items from the queue.
        """
        self._queue = []

class Stack:
    """
    A simple implementation of a LIFO stack.
    """
    
    def __init__(self):
        """
        Initialize the queue.
        """
        self._stack = []

    def __len__(self):
        """
        Returns: an integer representing the number of items in the queue.
        """
        return len(self._stack)

    def __str__(self):
        """
        Returns: a string representation of the queue.
        """
        string = ""
        for val in self._stack:
            string += str(val) + " "
        return string

    def push(self, item):
        """
        Add item to the queue.

        input:
            - item: any data type that's valid in a list
        """
        self._stack.append(item)

    def pop(self):
        """
        Remove the least recently added item.

        Assumes that there is at least one element in the queue.  It
        is an error if there is not.  You do not need to check for
        this condition.

        Returns: the least recently added item.
        """
        
        return self._stack.pop(len(self._stack)-1)

    def clear(self):
        """
        Remove all items from the queue.
        """
        self._stack = []


def bfs_dfs(graph, rac_class, start_node, end_node):
    """
    Performs a breadth-first search or a depth-first search on graph
    starting at the start_node.  The rac_class should either be a
    Queue class or a Stack class to select BFS or DFS.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - rac_class: a restricted access container (Queue or Stack) class to
          use for the search
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end

    Returns: a dictionary associating each visited node with its parent
    node.
    """
        
    rac = rac_class()
    dist = defaultdict(int)
    parent = defaultdict(str)
    for node in graph.nodes():
        dist[node] = float("inf")
        parent[node] = None
    dist[start_node] = 0
    rac.push(start_node)
    
    while len(rac)!=0:
        pop_node = rac.pop()
        for nbr in graph.get_neighbors(pop_node):
            if dist[nbr] == float("inf"):
                dist[nbr] = dist[pop_node]+1
                parent[nbr] = pop_node
                rac.push(nbr)
            if nbr == end_node:
                return dict(parent)
    
    return dict(parent)
   
    
def dfs(graph, start_node, end_node, parent):
    """
    Performs a recursive depth-first search on graph starting at the
    start_node.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end
        - parent: a dictionary that initially has one entry associating
                  the original start_node with None

    Modifies the input parent dictionary to associate each visited node
    with its parent node
    """
    if start_node == end_node:
        return
    if len(graph.get_neighbors(start_node))==0:
        return
    for nbr in graph.get_neighbors(start_node):
        if not nbr in parent.keys():
            parent[nbr]=start_node
            dfs(graph, nbr, end_node, parent)
    
    
    
   
print(dfs(maps.load_test_graph('line'), 'A', 'E', {'A': None}))
      
def smallest_f_node(open_set):
    """
    Returns the node with the smallest f.
    
    Inputs: open_set: a dictionary of nodes in the open set
    Outputs: the node with the smallest f
    """
    minimum = 0
    for node in open_set:
        minimum = open_set[node][0]
    for node in open_set:
        if open_set[node][0] < minimum:
            minimum = open_set[node][0]
    print("min:",minimum)        
    for node in open_set:
        if open_set[node][0]==minimum:
            return node
    return None

def output_closed(closed_set):
    """
    Returns a dictionary mapping each node in closed_set to its parent.
    
    Inputs: closed_set: a dictionary mapping each node to its f,g,h, and parent
    
    Outputs: a dictionary mapping each node to its parent
    """
    output_dict = {}
    if len(closed_set)!=0:
        for node in closed_set:
            output_dict[node]=closed_set[node][3]
    return output_dict

def astar(graph, start_node, end_node,
          edge_distance, straight_line_distance):
    """
    Performs an A* search on graph starting at start_node.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end
        - edge_distance: a function which takes two nodes and a graph
                         and returns the actual distance between two
                         neighboring nodes
        - straight_line_distance: a function which takes two nodes and
                         a graph and returns the straight line distance 
                         between two nodes

    Returns: a dictionary associating each visited node with its parent
    node.
    """
    open_set = {}
    closed_set = {}
    current_node = start_node
    open_set[current_node] = [0,0,0,None]
    while len(open_set)!=0:
        print("Openset: ",open_set)
        print("Closedset: ",closed_set)
        current_node = smallest_f_node(open_set)
        print("Currentnode:",current_node)
       
        if current_node == end_node:
            closed_set[current_node] = open_set.pop(current_node)
            return output_closed(closed_set)
        
        closed_set[current_node]=open_set.pop(current_node)
        print("Currentnode:",current_node)
        neighbors = graph.get_neighbors(current_node)
        print(neighbors)
        for nbr in neighbors:
            if not nbr in closed_set:
                if nbr in open_set:
                    
                    nbr_g = closed_set[current_node][1]+edge_distance(current_node,nbr,graph)
                    print("nbr_g:",nbr, nbr_g)
                    if open_set[nbr][1]>nbr_g:
                        open_set[nbr][1] = nbr_g
                        open_set[nbr][0] = straight_line_distance(nbr,end_node,graph)
                        open_set[nbr][3] = current_node
                
                else:
                    nbr_g = closed_set[current_node][1]+edge_distance(current_node,nbr,graph)
                    nbr_h = straight_line_distance(nbr,end_node,graph)
                    nbr_f = nbr_g+nbr_h
                    open_set[nbr] = [nbr_f,nbr_g,nbr_h,current_node]
                
       
    
    return output_closed(closed_set)