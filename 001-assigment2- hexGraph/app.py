from pickle import FALSE
from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import geometry as geo


app = Flask(__name__)
hops = hs.Hops(app)



@hops.component(
    "/createHexGraph",
    name = "Create Hexagonal Graph",
    inputs=[
        hs.HopsInteger("Count X", "X direction nodes", "Number of node in X", hs.HopsParamAccess.ITEM, default= 5),
        hs.HopsInteger("Count Y", "Y direction nodes", "Number of node in Y", hs.HopsParamAccess.ITEM, default= 5),
        hs.HopsInteger("Layout", "Layout", "Layout to order Nodes", hs.HopsParamAccess.ITEM, default= 0),
       # hs.HopsInteger("height", "h", "height of extrusion", hs.HopsParamAccess.ITEM),


    ],
    outputs=[
       hs.HopsPoint("Nodes","Nodes","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","Edges","List of Edges ", hs.HopsParamAccess.LIST),
      #hs.HopsSurface("Surface","S","List of Surfaces ", hs.HopsParamAccess.LIST)

    ]
)
def createGraph(X, Y, layout,):

    G = geo.createGridGraph(X, Y)
    GW = geo.addRandomWeights(G)


  



    nodes = geo.getNodes(GW, layout)
    edges = geo.getEdges(GW, layout) 

    #curve = rg.Curve.ToNurbsCurve(edges)
   # surface= rg.Extrusion.Create(curve,100,True)
    #surface= rg.Extrusion.Create(edges,100,FALSE)

    return nodes, edges# surface











if __name__== "__main__":
    app.run(debug=True)