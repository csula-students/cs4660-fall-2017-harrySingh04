"""
utils package is for some quick utility methods

such as parsing
"""
from . import graph as G
class Tile(object):
    """Node represents basic unit of graph"""
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

    def __str__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)
    def __repr__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.symbol == other.symbol
        return False
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self.x) + "," + str(self.y) + self.symbol)



def parse_grid_file(graph, file_path):
    """
    ParseGridFile parses the grid file implementation from the file path line
    by line and construct the nodes & edges to be added to graph

    Returns graph object
    """
    # TODO: read the filepaht line by line to construct nodes & edges
    f = open(file_path,encoding='utf-8')
    graphData = f.read()
    f.close()

    gridData = []
    #index = 0
    dataLine = graphData.split("\n")
    for data in dataLine:
        if data:
            #for i in range(1,len(data[1:-1]),2):
                #if not(data[i:i+2] == "--" ) :
                    #grid[index].append(data[i:i+2])
            gridData.append([data[i:i+2] for i in range(1,len(data[1:-1]),2)])
            #index+=1


    # Removing the -- data from the grid
    grid = gridData[1:-1]

    #print("Data for grid 0=",grid[0])
    totalNoTiles = {}
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            tile = Tile(x,y,grid[y][x])
            newNode = G.Node(tile)
            graph.add_node(newNode)
            totalNoTiles[(x,y)] = tile

    #print("totalNoTiles=",totalNoTiles)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            current_tile = Tile(x,y,grid[y][x])
            if current_tile.symbol == "##":
                continue

            if (x,y-1) in totalNoTiles:
                newTile = totalNoTiles[(x,y-1)]
                if (newTile.symbol != "##"):
                    graph.add_edge(G.Edge(G.Node(current_tile),G.Node(newTile),1))

            if (x,y+1) in totalNoTiles:
                newTile = totalNoTiles[(x,y+1)]
                if newTile.symbol != "##":
                    graph.add_edge(G.Edge(G.Node(current_tile),G.Node(newTile),1))

            if (x-1,y) in totalNoTiles:
                newTile = totalNoTiles[(x-1,y)]
                if newTile.symbol != "##":
                    graph.add_edge(G.Edge(G.Node(current_tile),G.Node(newTile),1))

            if (x+1,y) in totalNoTiles:
                newTile = totalNoTiles[(x+1,y)]
                if newTile.symbol != "##":
                    graph.add_edge(G.Edge(G.Node(current_tile),G.Node(newTile),1))


    return graph

def convert_edge_to_grid_actions(edges):
    """
    Convert a list of edges to a string of actions in the grid base tile

    e.g. Edge(Node(Tile(1, 2), Tile(2, 2), 1)) => "S"
    """

    #print("edges=",edges)
    path=""
    for edge in edges:
        fromTile = edge.from_node
        toTile = edge.to_node

        if(fromTile.data.x - toTile.data.x > 0):
            path+="E"
        elif(fromTile.data.y-toTile.data.y>0):
            path+="S"
        elif(fromTile.data.y-toTile.data.y<0):
            path+="N"
        elif(fromTile.data.x-toTile.data.x>0):
            path+="W"

    #print("path = ",path)
    return path
