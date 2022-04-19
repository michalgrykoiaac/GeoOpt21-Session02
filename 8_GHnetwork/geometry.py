import rhino3dm as rg
import networkx as nx
import random

def meshGraph(mesh,weightMode,X,Y):
    # Create graph
    G = nx.graph(X,Y)
    a=mesh

    for i in range(a.Vertices.Count):
        # Get vertex as point3D
        pt3D=rg.Point3d(a.Vertices[i])
        # Add node to graph and get its neighbours
        g.add_node(i,point=pt3D)
        neighbours = a.Vertices.GetConnectedVertices(i)
        # Add edges to graph
        for n in neighbours:  
            if n > i:
                p1=rg.Point3d.FromPoint3f(a.Vertices[i])
                p2=rg.Point3d.FromPoint3f(a.Vertices[n])
                line = rg.Line(p1,p2)
                if weightMode == "edgeLength":
                        w = line.Length
                elif weightMode == "sameWeight":
                        w = 1
                g.add_edge(i,n,weight=w,line=line)

    Nodes = [g.nodes[i]["point"] for i in g.nodes()]
    Edges = [e[2]["line"] for e in g.edges(data=True)]

    
   # N.getBoundingBox()
    #G.add_nodes_from([1,3])
    G.add_node(Nodes)
    G.add_edge(Edges)
    return nx.draw(G)