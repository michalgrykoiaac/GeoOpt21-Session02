#we import all the libraries that our functions need here too
import random as r
import rhino3dm as rg
import geometry as geo

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

def createExtrusion(p1,p2, p3, h, uDiv=2, ss=5):
 
   
    curve = rg.Curve.CreateControlPointCurve([p1,p2,p3],2)
    
    surface = rg.Extrusion.Create(curve,h,False)

    spheres=[]
    uCurves = []
    vCurves = []
    vDiv =2
    #Domain
    domain = rg.Interval(0,1)
    surface.SetDomain(0, domain)
    surface.SetDomain(1, domain)

    #Isocurve Extraction
    for u in range(uDiv):
        if u == 0 or u/uDiv == 1:
            continue
        else:
            uCurve = surface.IsoCurve(1, u/uDiv)
            uCurves.append(uCurve)

    for v in range(vDiv):
        if v == 0 or v/vDiv == 1:
            continue
        else:
            vCurve = surface.IsoCurve(0, v/vDiv)
            vCurves.append(vCurve)

    for c in uCurves:
        startPoint = c.PointAtEnd
        s = rg.Sphere(startPoint,ss)
        sphere = s.ToBrep()
        spheres.append(sphere)

    

    return  uCurves, curve, spheres