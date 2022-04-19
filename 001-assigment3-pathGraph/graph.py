import rhino3dm as rg
import networkx as nx


def createGridGraph(x, y):

    M = nx.grid_2d_graph(x,y)
    return M

def getNodes(G, layout = 0):

    if layout == 0 : lay =  nx.kamada_kawai_layout(G)
    elif layout == 1 : lay =  nx.circular_layout(G)
    elif layout == 2 : lay =  nx.shell_layout(G)
    elif layout == 3 : lay =  nx.spiral_layout(G)
    else: lay = nx.planar_layout(G)

    nodes = []
    for d in lay.values():
        pt = rg.Point3d( d[0], d[1] , 0)
        nodes.append(pt)

    return nodes


def getEdges(G, layout = 0):

    if layout == 0 : lay =  nx.kamada_kawai_layout(G)
    elif layout == 1 : lay =  nx.circular_layout(G)
    elif layout == 2 : lay =  nx.shell_layout(G)
    elif layout == 3 : lay =  nx.spiral_layout(G)
    else: lay = nx.planar_layout(G)

    edges = []
    for e in G.edges:
        p1 = rg.Point3d( lay[e[0]][0], lay[e[0]][1], 0 )
        p2 = rg.Point3d( lay[e[1]][0], lay[e[1]][1], 0 )
        line = rg.LineCurve(p1, p2)
        edges.append(line)

    return edges



G = createGridGraph(3,3)

nodes = getNodes(G)
edges = getEdges(G)