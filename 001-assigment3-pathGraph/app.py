from flask import Flask
import ghhops_server as hs


import geometry as geo

import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/pathGraphNetwork",
    name = "Create organic path network",
    inputs=[
        hs.HopsPoint("Points", "points", "network points", hs.HopsParamAccess.LIST),
        hs.HopsCurve("Curve", "curves", "network curves", hs.HopsParamAccess.LIST),
        hs.HopsInteger("Layout", "layout", "Layout to order Nodes", hs.HopsParamAccess.ITEM, default= 0),
    ],
    outputs=[
       hs.HopsPoint("Nodes","Nodes","converted nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","Edges","converted edges ", hs.HopsParamAccess.LIST)
    ]
)

def createPathGraphNetwork(points, curves, layout):

    G = geo.pathGraphNetwork(points, curves, layout)

    nodes = geo.getNodes(G)
    edges = geo.getEdges(G) 

    return nodes, edges


if __name__== "__main__":
    app.run(debug=True)