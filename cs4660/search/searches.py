"""
Searches module defines all different search algorithms
"""
#from datastructure import structure
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


def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    for neighbor_nodes in graph.neighbors(initial_node):
        if neighbor_nodes == dest_node:
            return [graph.get_edge(initial_node,dest_node)]
        else:
            edge_path = dfs(graph,neighbor_nodes,dest_node)
            if edge_path != []:
                list = [graph.get_edge(initial_node,neighbor_nodes)]
                list.extend(edge_path)
                return list

    return []

def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    # dictionary key variable to store the distance between the two nodes
    distance_node = {}
    # list to store the list of nodes visited
    visited_nodes = []
    # Dictionar key variable to store the list of parents of node visited
    parent_list = {}
    Q = []
    distance_node[initial_node] = 0
    parent_list[initial_node] = None
    Q.append((0,initial_node))
    while(bool(Q)):
        Q = sorted(Q, key=lambda x: x[0])
        min_node =[Q.pop(0)]
        cur_node = min_node[0][1]
        visited_nodes.append(cur_node)
        for neighbor_nodes in graph.neighbors(cur_node):
            if neighbor_nodes not in visited_nodes:
                if neighbor_nodes not in distance_node:
                    distance_node[neighbor_nodes] = distance_node[cur_node] + graph.distance_nodes(cur_node,neighbor_nodes)
                    value = distance_node[neighbor_nodes]
                    Q.append((value,neighbor_nodes))
                    parent_list[neighbor_nodes] = cur_node
                else:
                    if distance_node[neighbor_nodes] > (distance_node[cur_node] + graph.distance_nodes(cur_node,neighbor_nodes)):
                        distance_node[neighbor_nodes] = distance_node[cur_node] + graph.distance_nodes(cur_node,neighbor_nodes)
                        value = distance_node[neighbor_nodes]
                        Q.append((value,neighbor_nodes))
                        parent_list[neighbor_nodes] = cur_node
        if dest_node in visited_nodes:
            break


    list = []
    start_node = dest_node
    while(parent_list[start_node] is not None):
        par_node = parent_list[start_node]
        #print("parent node",par_node)
        edge = graph.get_edge(par_node,start_node)
        #print("edge",edge)
        list.append(edge)
        start_node = par_node


    list.reverse()
    return list


def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    # dictionary key variable to store the distance between the two nodes
    distance_node = {}
    # dictionary key to store the heirustic distance
    heuristicDistance = {}
    # list to store the list of nodes visited
    visited_nodes = []
    # Dictionar key variable to store the list of parents of node visited
    parent_list = {}
    Q = {}
    start_dist = calculateEuclidianDistance(initial_node,dest_node)
    distance_node[initial_node] = 0
    heuristicDistance[initial_node] = start_dist
    parent_list[initial_node] = None
    priorityKey = distance_node[initial_node] + heuristicDistance[initial_node]
    Q[initial_node] = 0
    #print(" Graph data =",graph.adjacency_list[initial_node])
    while(bool(Q)):
        min_node =min(Q.items(), key=lambda x: x[1])
        #print(min_node)

        #if dest_node.data.symbol == "@5":
            #print("The queue data is = ",Q.items(),"\n\n")
            #print("Starting distane = ",start_dist,"\n\n")
            #print("Distance  = ",distance_node[min_node[0]],"\n\n")
            #print("heuristicDistance = ", heuristicDistance[min_node[0]],"\n\n\n")

            #print("neighbors of me = ",graph.neighbors(min_node[0]))
            #print("visited_nodes = ",visited_nodes,"\n\n\n\n")
            #if min_node[0] in visited_nodes:
                #print("you are here again")

        cur_node = min_node[0]
        Q.pop(cur_node)
        #print(" Current node = ",cur_node)
        if cur_node in visited_nodes:
            #print("you are here again")
            continue
        visited_nodes.append(cur_node)
        #print(initial_node)
        count=0;
        for neighbor_nodes in graph.neighbors(cur_node):
            if neighbor_nodes not in visited_nodes:
                distance = calculateEuclidianDistance(neighbor_nodes,dest_node)
                if neighbor_nodes not in distance_node:
                    distance_node[neighbor_nodes] = distance_node[cur_node] + graph.distance_nodes(cur_node,neighbor_nodes)
                    heuristicDistance[neighbor_nodes] = distance
                    priorityKey = graph.distance_nodes(cur_node,neighbor_nodes) + heuristicDistance[neighbor_nodes]
                    Q[neighbor_nodes]=priorityKey
                    parent_list[neighbor_nodes] = cur_node
                else:
                    if distance_node[neighbor_nodes] > (distance_node[cur_node] + graph.distance_nodes(cur_node,neighbor_nodes)):
                        distance_node[neighbor_nodes] = distance_node[cur_node] + graph.distance_nodes(cur_node,neighbor_nodes)
                        heuristicDistance[neighbor_nodes] = distance
                        priorityKey = graph.distance_nodes(cur_node,neighbor_nodes) + heuristicDistance[neighbor_nodes]
                        Q[neighbor_nodes]=priorityKey
                        parent_list[neighbor_nodes] = cur_node
        if dest_node in visited_nodes:
            #print(" I have found you \n\n\n\n\n\n\n\n\n\n")
            break


    list = []
    start_node = dest_node
    while(parent_list[start_node] is not None):
        par_node = parent_list[start_node]
        #print("parent node",par_node)
        edge = graph.get_edge(par_node,start_node)
        #print("edge",edge)
        list.append(edge)
        start_node = par_node


    list.reverse()
    return list

def calculateEuclidianDistance(node1,node2):
    node1x = node1.data.x
    node1y = node1.data.y
    node2x = node2.data.x
    node2y = node2.data.y

    ed_distance = ((node1x-node2x)**2 + (node1y-node2y)**2)**0.5
    return ed_distance
