import rhinoinside
import ghhops_server as hs
import rhino3dm
rhinoinside.load() #this is new. This allows us to import Rhino and Rhino.Geometry

import Rhino 
import Rhino.Geometry as rg
#hops = hs.Hops(app=rhinoinside) #this is new
from pickle import FALSE
from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import geometry as geo
import networkx as nx

app = Flask(__name__)
hops = hs.Hops(app)


import networkx as nx
import MeshPaths as mp

@hops.component(
    "/MeshPathWalker",
    name="MeshPathWalker",
    description=" Make a networkx graph with mesh vertices as nodes and mesh edges as edges ",
    inputs=[
        hs.HopsMesh("Mesh","M","Mesh to make networkx graph for"),
        hs.HopsString("WeightMode ","W","Weight Mode"),
        hs.HopsString("GraphType","T","Mesh Graph Type"),
        hs.HopsLine("SLine","L", "Line to process"),
        hs.HopsString("mode" ,"m", "Shortest Path Mode")
    ],
    outputs=[
        hs.HopsPoint("ShortestPath", "SP" ,"Shortest Path",hs.HopsParamAccess.LIST),
        hs.HopsString("FacesIndex", "I" ,"Faces indexes",hs.HopsParamAccess.LIST)
    ]
)

def MeshPathWalker(mesh,weightMode,GraphType,SLine,mode):
    return mp.meshwalker(mesh,weightMode,GraphType,SLine,mode)

if __name__ == "__main__":
    hops.start()