import rhino3dm as rg
import networkx as nx

#pseudo code
#identify unique points and add them as nodes to network
#extract start and end points of lines
#determine which node the start or end point matches to
#add network edge

def createGridGraph(points, lines):
    G = nx.Graph()
    ptCoords = []

    for i in range(len(points)):
        G.add_node(i)
        ptCoords.append((round(points[i].X, 3), round(points[i].Y, 3), round(points[i].Z, 3)))
        print(ptCoords)
    
    for i in range(len(lines)):
        print(lines[i].PointAtStart)
        print((round(lines[i].PointAtStart.X, 3), round(lines[i].PointAtStart.Y,3), round(lines[i].PointAtStart.Z,3)))
        startNode = ptCoords.index((round(lines[i].PointAtStart.X,3), round(lines[i].PointAtStart.Y,3), round(lines[i].PointAtStart.Z,3)))
        endNode = ptCoords.index((round(lines[i].PointAtEnd.X,3), round(lines[i].PointAtEnd.Y,3), round(lines[i].PointAtEnd.Z,3)))
        G.add_edge(startNode, endNode)

    return G

def getNodes(Kite):

    lay =  nx.kamada_kawai_layout(Kite)

    nodes = []
    for d in lay.values():
        pt = rg.Point3d( d[0], d[1] , 0)
        nodes.append(pt)

    return nodes

def getEdges(G):

    lay =  nx.kamada_kawai_layout(G)

    edges = []
    for e in G.edges:
        p1 = rg.Point3d( lay[e[0]][0], lay[e[0]][1], 0 )
        p2 = rg.Point3d( lay[e[1]][0], lay[e[1]][1], 0 )
        line = rg.LineCurve(p1, p2)
        edges.append(line)

    return edges


"""
G = createGridGraph(3,3)
GW = addRandomWeigrhs(G)
nodes = getNodes(G)
edges = getEdges(G)