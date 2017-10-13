"""
Searches module defines all different search algorithms
"""
def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    # Queue to store the list of node which will be going to be visited
    Q = []
    # list to store the list of nodes visited
    visited_nodes = []
    # Dictionar key variable to store the list of parents of node visited
    parent_list = {}
    # dictionary key variable to store the distance between the two nodes
    distance_node = {}
    # Adding the intial node into the list
    distance_node[initial_node] = 0
    parent_list[initial_node]= None
    Q.append(initial_node)
    while(bool(Q)):
        cur_node = Q.pop(0)
        for neighbor_nodes in graph.neighbors(cur_node):
            if neighbor_nodes not in visited_nodes:
                visited_nodes.append(neighbor_nodes)
                parent_list[neighbor_nodes] = cur_node
                distance_node[neighbor_nodes] = distance_node[cur_node] + graph.distance_nodes(cur_node,neighbor_nodes)
                Q.append(neighbor_nodes)

        if dest_node in visited_nodes:
            break

    list = []
    start_node = dest_node
    #print("parent list =",parent_list)

    #for cur_node,par_node in parent_list.items():
    #    if par_node is not None:
    #        edge = graph.get_edge(par_node,cur_node)
    #        print("edge",edge)
    #        list.append(edge)
    while(parent_list[start_node] is not None):
        par_node = parent_list[start_node]
        #print("parent node",par_node)
        edge = graph.get_edge(par_node,start_node)
        #print("edge",edge)
        list.append(edge)
        start_node = par_node


    list.reverse()
    return list










    pass

def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass

def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass

def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass
