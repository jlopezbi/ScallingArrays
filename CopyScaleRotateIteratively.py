# COPY AND SCALE PARTS, ROTATE,
import rhinoscriptsyntax as rs

def copyAndScale():
    numCopies = rs.GetReal("type number of copies", 1, 1)
    scale = rs.GetReal("type scale factor", .8, .1, 1.5)
    angle = rs.GetReal("angle for spiral", 20, -180, 180)
    objectIds = rs.GetObjects("select objects to copy and scale",0,True,True)
    startPnt = rs.GetPoint("point to copy from")
    endPnt = rs.GetPoint("point to move to")
    
    translationVec = endPnt-startPnt
    
    if objectIds and startPnt and endPnt and scale and numCopies and angle:
        for i in range(int(numCopies)):
            startPnt += translationVec
            objectsTemp = rs.CopyObjects(objectIds, translationVec)
            rs.ScaleObjects(objectsTemp, startPnt, [scale]*3)
            rs.RotateObjects(objectsTemp, startPnt, angle)
            objectIds = objectsTemp

            translationVec = rs.VectorScale(translationVec, scale)
            translationVec = rs.VectorRotate(translationVec, angle, (0,0,1))

    

           

            
if __name__=="__main__":
    copyAndScale()
