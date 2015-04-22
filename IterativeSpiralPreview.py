#COPY,SCALE,ROTATE, preview
## work in progress ##
import rhinoscriptsyntax as rs

def copyScaleRotate():
    baseObjects = rs.GetObjects("select objects to copy and scale",0,True,True)
    startPnt = rs.GetPoint("point to copy from")
    endPnt = rs.GetPoint("point to move to")


    translationVec = endPnt-startPnt
    scale = .8
    angle = 30
    numCopies = 6

    preview = []
    while True:
        rs.EnableRedraw(False)
        
        for p in preview: rs.DeleteObjects(p)
        preview = []
        obj = generateSpiral(baseObjects, scale, angle, startPnt, translationVec,
                             numCopies)
        preview.append(obj)
        rs.EnableRedraw(True)

        result = rs.GetString("Spiral Settings", "Accept", ("scale", "angle",
                                                        "location", "copies", "Accept"))
        if not result:
            rs.DeleteObjects(obj)
            break
        result = result.upper()
        if result == "ACCEPT": break
        elif result == "SCALE":
            scaleTemp = rs.GetReal("type scale factor", .8, .1, 1.5)
            if scaleTemp: scale = scaleTemp
        elif result == "ANGLE":
            angleTemp = rs.GetReal("angle for spiral", 20, -180, 180)
            if angleTemp: angle = angleTemp
        elif result == "LOCATION":
            startPntTemp = rs.GetPoint("point to copy from")
            endPntTemp = rs.GetPoint("point to move to")
            if startPntTemp and endPntTemp:
                startPnt  = startPntTemp
                translationVec = endPntTemp - startPnt
        elif result == "COPIES":
            copiesTemp = rs.GetReal("number of copies", 6,1,300)
            if copiesTemp: numCopies = copiesTemp


def generateSpiral(objectIds, scale, angle, startPnt, translationVec, numCopies):
    allGeometry = []
    for i in range(int(numCopies)):
        startPnt += translationVec
        objectsTemp = rs.CopyObjects(objectIds, translationVec)
        rs.ScaleObjects(objectsTemp, startPnt, [scale]*3)
        rs.RotateObjects(objectsTemp, startPnt, angle)
        objectIds = objectsTemp

        if objectsTemp: allGeometry.append(objectsTemp)

        translationVec = rs.VectorScale(translationVec, scale)
        translationVec = rs.VectorRotate(translationVec, angle, (0,0,1))
    return allGeometry

if __name__=="__main__":
    copyScaleRotate()
