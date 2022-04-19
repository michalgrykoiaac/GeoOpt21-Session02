from pickle import FALSE
from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import geometry as geo
import networkx as nx


app = Flask(__name__)
hops = hs.Hops(app)



@hops.component(
    "/createPathGraph",
    name = "Create Graph",
    inputs=[
        hs.HopsInteger("Count X", "X", "Number of node in X", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Count Y", "Y", "Number of node in Y", hs.HopsParamAccess.ITEM, default= 1),
        #hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       #hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST),
       hs.HopsMesh("Mesh","M","Mesh to make networkx graph for"),
        hs.HopsString("WeightMode ","W","Weight Mode")


    ]
   # outputs=[
     #  hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
      # hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST),
     

    #]
)



#def createPathGraph(X, Y):

   # G = nx.graph(X,Y)
   # N.getBoundingBox()
   # G.add_nodes_from([1,3])
   # return G


#nx.draw(G)

def MeshGrapher(X,Y, mesh,weightMode):
    return nx.meshGraph(X,Y, mesh,weightMode)







if __name__== "__main__":
    app.run(debug=True)