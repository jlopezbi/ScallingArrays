# COPY AND SCALE PARTS
import rhinoscriptsyntax as rs

def copyAndScale():
    numCopies = rs.GetReal("type number of copies", 1, 1)
    scale = rs.GetReal("type scale factor", .8, .1, 1.5)
    objectIds = rs.GetObjects("select objects to copy and scale", 0, True)
    startPnt = rs.GetPoint("point to copy from")
    endPnt = rs.GetPoint("point to move to")
    
    translationVec = endPnt-startPnt
    
    if objectIds and startPnt and endPnt and scale and numCopies:
        for i in range(int(numCopies)):
            startPnt += translationVec
            objectsTemp = rs.CopyObjects(objectIds, translationVec)
            rs.ScaleObjects(objectsTemp, startPnt, [scale]*3)
            objectIds = objectsTemp

            translationVec = rs.VectorScale(translationVec, scale)

    

           

            
if __name__=="__main__":
    copyAndScale()
