"""
quiz2!
Use path finding algorithm to find your way through dark dungeon!
Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9
TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import json

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.
    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = json.load(urlopen(req, jsondataasbytes))
    return response
#Implementing BFS search

def BFS_Search(empty_room,dest_room):
    start_node = empty_room['id']
    dest_node = dest_room['id']
    print("dest_node",dest_node)
    # Queue to store the list of node which will be going to be visited
    Q = []
    # list to store the list of nodes visited
    visited_nodes = []
    # Dictionar key variable to store the list of parents of node visited
    parent_list = {}
    # dictionary key variable to store the distance between the two nodes
    hp_point = {}
    # Adding the intial node into the list
    hp_point[start_node] = 0
    parent_list[start_node]= None
    Q.append(start_node)
    while((bool(Q))):
        cur_node = Q.pop(0)
        if cur_node != start_node:
            neighbors = get_state(cur_node)
            #print("neighbors = ",neighbors)
        else:
            neighbors = empty_room

        if len(neighbors)>0:
            for i in range(len(neighbors)):
                neighbor_nodes = neighbors['neighbors'][i]['id']
                if neighbor_nodes not in visited_nodes:
                    visited_nodes.append(neighbor_nodes)
                    parent_list[neighbor_nodes] = cur_node
                    trans_weight = (transition_state(cur_node, neighbors['neighbors'][i]['id']))
                    #print("trans_weight =",trans_weight)
                    hp_point[neighbor_nodes] = hp_point[cur_node] + trans_weight['event']['effect']
                    #print("neighbors = ",neighbor_nodes,"\n\n\n\n\n\n")
                    Q.append(neighbor_nodes)
                    #print("Items = ",Q)

        if dest_node in visited_nodes:
            print("visited_nodes",visited_nodes)
            break

    #print("WE have items=",Q)
    print("HP epoint = ",parent_list)
    list = []
    total_hp_bfs=0
    start_node = dest_node
    while(parent_list[start_node] is not None):
        par_node = parent_list[start_node]
        #print("parent node",par_node)
        total_hp_bfs += hp_point[par_node]
        start_node = par_node

    return total_hp_bfs

def Dijkstra(empty_room,dest_room):
    start_node = empty_room['id']
    dest_node = empty_room['id']
    # dictionary key variable to store the distance between the two nodes
    distance_node = {}
    # list to store the list of nodes visited
    visited_nodes = []
    # Dictionar key variable to store the list of parents of node visited
    parent_list = {}
    Q = []
    hp_effect[start_node] = 0
    parent_list[start_node] = None
    Q.append((0,start_node))
    while(bool(Q)):
        sorted(Q, key=lambda x: x[0],reverse = True)
        max_node =[Q.pop(0)]
        cur_node = max_node[0][1]
        if cur_node in visited_nodes:
            continue
        visited_nodes.append(cur_node)
        if cur_node != start_node:
            neighbors = get_state(cur_node)
            #print("neighbors = ",neighbors)
        else:
            neighbors = empty_room
        for i in range(len(neighbors['neighbors'])):
            neighbor_nodes = neighbors['neighbors'][i]['id']
            if neighbor_nodes not in visited_nodes:
                if neighbor_nodes not in hp_point:
                    trans_weight = (transition_state(cur_node, neighbors['neighbors'][i]['id']))
                    print("trans_weight =",trans_weight)
                    hp_point[neighbor_nodes] = hp_point[cur_node] + trans_weight['event']['effect']
                    value = hp_point[neighbor_nodes]
                    Q.append((value,neighbor_nodes))
                    parent_list[neighbor_nodes] = cur_node
                else:
                    if hp_point[neighbor_nodes] > (hp_point[cur_node]) + (transition_state(cur_node, neighbors['neighbors'][i]['id'])):
                        hp_point[neighbor_nodes] = hp_point[cur_node] + (transition_state(cur_node, neighbors['neighbors'][i]['id']))
                        value = hp_point[neighbor_nodes]
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

    return 0

if __name__ == "__main__":
    # Your code starts here
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    dest_room = get_state('f1f131f647621a4be7c71292e79613f9')
    #print(empty_room['id'])
    #print("my neighbors",empty_room['neighbors'])
    #print("length = ",len(empty_room['neighbors']))
    #print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))
    #Calling method BFS search
    print(BFS_Search(empty_room,dest_room))
    print(Dijkstra(empty_room,dest_node))
