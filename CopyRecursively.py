import rhinoscriptsyntax as rs
# CopyUnits Recursively WORK IN PROGRESS

def recursiveCopy():
    obj = rs.GetObjects("select group to act as base unit")
    lineTrans = rs.GetObject("select line for translation")
    depth = rs.GetReal("number of copies",10,2,20)
    scale = rs.GetReal("scale factor",.8,.2,.9)
    
    if obj is None: return
    if lineTrans is None: return
    if depth is None: return
    if scale is None: return

def copy(obj, depth, vecLoc, rotPnt, theta, scale):
    if depth >0:
        depth -=1
        #make copy and translate
        newObj = rs.CopyObject(obj, (vecLoc))
        #rotate by theta
        rs.RotateObject(obj, rotPnt, theta)
        

    
