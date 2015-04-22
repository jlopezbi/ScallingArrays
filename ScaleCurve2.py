import rhinoscriptsyntax as rs
# scale and copy curve, loft curves to make a surface

def scaleCurve():
    curve_id = rs.GetObject("Select a curve to copy and scale", 4, True, True)
    if curve_id is None: return

    length = rs.CurveLength(curve_id)

    lengthLimit = rs.GetReal("Length limit", 2, 0.01, length)
    scaleFactor = rs.GetReal("Scale Factor", .7, .01,.99999)
    if lengthLimit is None: return
    if scaleFactor is None: return

    y = 1
    z = 1
    sections = [curve_id]
    while True:
        if rs.CurveLength(curve_id)<=lengthLimit: break
        curve_id = rs.ScaleObject(curve_id, (0,y,z), (scaleFactor,scaleFactor,scaleFactor
                                                      ), True)
        sections.append(curve_id)
        z+=1
        if curve_id is None:
            print "Something went wrong..."
            return
    if not sections: return
    rs.AddLoftSrf(sections)
    
        
if __name__=="__main__":
    scaleCurve()
