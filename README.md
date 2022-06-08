# Map-Search
Searches a street map to find a route from a start point to an end point.

Implements Breadth-First Search, Recursive Depth-First Search, and A* Search in stacks, graphs, and queues. 


1. Modify BFS 
The graphs in this assignment are each represented as an instance of the DiGraph class.  A DiGraph object is a directed graph.  The DiGraph class is defined in the comp140_module7_graphs module. 

2. Implement Recursive DFS
Implements the function bfs_dfs(graph, rac_class, start_node, end_node). The graph parameter is a DiGraph object that represents the street graph. The rac_class parameter is a restricted access container (RAC) class (Queue or Stack).  The start_node and end_node parameters should be nodes in graph.  The bfs_dfs function returns a dictionary mapping nodes in graph to their parents.


Implements the function dfs(graph, start_node, end_node, parent). The graph parameter is a DiGraph object that represents the street graph. The start_node and end_node parameters should be nodes in graph. The parent parameter is a dictionary mapping each node in graph that has already been explored to its parent. When called initially, parent will map start_node to None.  The dfs function should modify parent appropriately as it runs. Each function invocation looks only at the neighbors of a single node in graph.


3. Implement A*
Implement the function astar(graph, start_node, end_node, edge_distance, straight_line_distance). The graph parameter should be a DiGraph object that represents the street graph. The start_node and end_node parameters should be nodes in graph. The edge_distance and straight_line_distance parameters are the distance functions you should use. Each of these distance functions takes three parameters: node1, node2, and graph.  The edge_distance function returns the actual distance required to travel from node1 to node2 in graph, if the two nodes are neighbors.  The straight_line_distance function returns the heuristic distance from node1 to node2, where node2 does not need to be a neighbor of node1 in graph; if it is, this function returns the straight line distance between them. The astar function should return a dictionary mapping nodes in graph to their parents.

