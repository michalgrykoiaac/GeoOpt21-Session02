from flask import Flask
import ghhops_server as hs

#notice, we import another file as a library
import geometry as geo

#we also import random library to generate some randomness 
import random as r

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)



@hops.component(
    "/createTreeLine",
    name = "Create Tree Line",
    inputs=[
        hs.HopsPoint( "p1","point 1", "Point 1 of curve", hs.HopsParamAccess.ITEM),
        hs.HopsPoint( "p2","point 2", "Point 2 of curve", hs.HopsParamAccess.ITEM),
        hs.HopsPoint( "p3","point 3", "Point 3 of curve", hs.HopsParamAccess.ITEM),
        hs.HopsInteger( "h", "height","Height of tree (m)", hs.HopsParamAccess.ITEM),
        hs.HopsInteger(  "uDiv","tree number","Number of Tree", hs.HopsParamAccess.ITEM),
        hs.HopsInteger(  "ss","canopy size","sphere size (m)", hs.HopsParamAccess.ITEM)

    ],
    outputs=[
       #hs.HopsSurface("Random Points","surface","List of generated random points ", hs.HopsParamAccess.ITEM),
       hs.HopsCurve("path curve","path curve","path curve ", hs.HopsParamAccess.ITEM),
       hs.HopsCurve("tree trunk","tree trunk","tree trunk ", hs.HopsParamAccess.LIST),
       #hs.HopsCurve("curves","vCurves","curves ", hs.HopsParamAccess.LIST),
       hs.HopsBrep("spheres","tree canopy","tree ", hs.HopsParamAccess.LIST),
    ]
)
def moreExtrusion(p1,p2, p3,h, uDiv, ss):

    #surfaces = geo.createExtrusion(p1, p2, p3, h, uDiv,ss)[0]
    uCurves = geo.createExtrusion(p1, p2, p3, h, uDiv,ss)[0]
    curve = geo.createExtrusion(p1, p2, p3, h, uDiv,ss)[1]
  
    spheres = geo.createExtrusion(p1, p2, p3, h, uDiv,ss)[2]
   # vCurves = geo.createExtrusion(p1, p2, h, uDiv, vDiv)[2]
    return  uCurves, curve, spheres #vCurves,



if __name__== "__main__":
    app.run(debug=True)