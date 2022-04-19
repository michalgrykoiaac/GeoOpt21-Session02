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
    "/createRandomPoints",
    name = "Create Random Points",
    inputs=[
        hs.HopsInteger("Count", "C", "Number of Random Points", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsNumber("X range of randomness", "X", "Maximum randomness in X directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Y range of randomness", "Y", "Maximum randomness in Y directon", hs.HopsParamAccess.ITEM)

    ],
    outputs=[
       hs.HopsPoint("Random Points","RP","List of generated random points ", hs.HopsParamAccess.LIST)
    ]
)
def createRandomPoints(count,rX, rY):

    randomPts = []
    for i in range(count):

        #in each itereation generate some random points
        random_x = r.uniform(-rX, rX)
        random_y = r.uniform(-rY, rY)

        #create a point with rhino3dm
        random_pt = rg.Point3d(random_x, random_y, 0)
        
        #add point to the list
        randomPts.append(random_pt)

    return randomPts



@hops.component(
    "/moreRandomPoints",
    name = "More Random Points",
    inputs=[
        hs.HopsInteger("Count", "C", "Number of Random Points", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsNumber("X range of randomness", "X", "Maximum randomness in X directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Y range of randomness", "Y", "Maximum randomness in Y directon", hs.HopsParamAccess.ITEM)

    ],
    outputs=[
       hs.HopsPoint("Random Points","RP","List of generated random points ", hs.HopsParamAccess.LIST)
    ]
)
def moreRandomPoints(count,rX, rY):

    randomPts = geo.createRandomPoints(count, rX, rY)
    return randomPts



@hops.component(
    "/createTreeLine",
    name = "Create Tree Line",
    inputs=[
        hs.HopsPoint( "p1","point 1", "Point 1 of curve", hs.HopsParamAccess.ITEM),
        hs.HopsPoint( "p2","point 2", "Point 2 of curve", hs.HopsParamAccess.ITEM),
        hs.HopsPoint( "p3","point 3", "Point 3 of curve", hs.HopsParamAccess.ITEM),
        hs.HopsInteger( "h", "height","Height of tree", hs.HopsParamAccess.ITEM),
        hs.HopsInteger(  "uDiv","tree number","Number of Tree", hs.HopsParamAccess.ITEM),
        hs.HopsInteger(  "ss","canopy size","sphere size", hs.HopsParamAccess.ITEM)

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