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
    #print("dest_node",dest_node)
    # Queue to store the list of node which will be going to be visited
    Q = []
    # list to store the list of nodes visited
    visited_nodes = []
    # Dictionar key variable to store the list of parents of node visited
    parent_list = {}
    # dictionary key variable to store the distance between the two nodes
    distance_node = {}
    # Adding the intial node into the list
    distance_node[start_node] = 0
    parent_list[start_node]= None
    Q.append(start_node)
    while((bool(Q))):
        cur_node = Q.pop(0)
        neigh = get_state(cur_node)
        neighbor_nodes = neigh['neighbors']
        for i in range(len(neighbor_nodes)):
            neighbors = neighbor_nodes[i]['id']
            if neighbor_nodes not in visited_nodes:
                visited_nodes.append(neighbors)
                parent_list[neighbors] = cur_node
                distance_node[neighbors] = distance_node[cur_node]+1
                Q.append(neighbors)

        if dest_node in visited_nodes:
            #print("visited_nodes",visited_nodes)
            break

    #print("WE have items=",Q)
    #print("HP epoint = ",parent_list)
    #list = []
    total_hp_bfs=0
    start_node = dest_node
    if dest_node in visited_nodes:
        #print("found you")
        total_hp_bfs = distance_node[dest_node]

    return total_hp_bfs

def Dijkstra(empty_room,dest_room):
    start_node = empty_room['id']
    dest_node = dest_room['id']
    # dictionary key variable to store the distance between the two nodes
    distance_node = {}
    # list to store the list of nodes visited
    visited_nodes = []
    # Dictionar key variable to store the list of parents of node visited
    parent_list = {}
    Q = []
    distance_node[start_node] = 0
    parent_list[start_node] = None
    Q.append((0,start_node))
    while(bool(Q)):
        Q = sorted(Q, key=lambda x: x[0],reverse = True)
        #print("items",Q,"\n\n\n")
        max_node =[Q.pop(0)]
        #print("Max node = ",max_node,"\n\n\n")
        cur_node = max_node[0][1]
        if cur_node in visited_nodes:
            #print("visited_nodes",visited_nodes)
            continue
        visited_nodes.append(cur_node)
        neigh = get_state(cur_node)
        neighbor_nodes = neigh['neighbors']
        for i in range(len(neighbor_nodes)):
            neighbors = neighbor_nodes[i]['id']
            if neighbors not in visited_nodes:
                trans_weight = (transition_state(cur_node, neighbors))
                hp_weight = trans_weight['event']['effect']
                #print(distance_node[cur_node] + trans_weight['event']['effect'])
                if neighbors not in distance_node:
                    #print("trans_weight =",trans_weight)
                    distance_node[neighbors] = distance_node[cur_node]+ hp_weight
                    value = distance_node[neighbors]
                    Q.append((value,neighbors))
                    parent_list[neighbors] = cur_node
                else:
                    if distance_node[neighbors] < distance_node[cur_node] + hp_weight:
                        distance_node[neighbors] = distance_node[cur_node] + hp_weight
                        value = distance_node[neighbors]
                        Q.append((value,neighbors))
                        parent_list[neighbors] = cur_node
        if dest_node in visited_nodes:
            break

    hp_point_dijkstra = 0;
    if dest_node  in visited_nodes:
        hp_point_dijkstra = distance_node[dest_node]

    return hp_point_dijkstra

if __name__ == "__main__":
    # Your code starts here
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    dest_room = get_state('f1f131f647621a4be7c71292e79613f9')
    #print(empty_room['id'])
    #print("my neighbors",empty_room['neighbors'])
    #print("length = ",len(empty_room['neighbors']))
    #print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))
    #Calling method BFS search
    hp_point_bfs = BFS_Search(empty_room,dest_room)
    print("Hp point for BFS = ",hp_point_bfs)
    hp_point_dijkstra = Dijkstra(empty_room,dest_room)
    print("HP point for Dijkstra=",hp_point_dijkstra)
