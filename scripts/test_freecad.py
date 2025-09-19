
# execute in console with
#   

import FreeCAD

doc = FreeCAD.ActiveDocument
if doc is None:
    print("No active document.")
else:
    for obj in doc.Objects:
        if obj.TypeId.lower().startswith('part::'):
            length = getattr(obj, 'Length', None)
            height = getattr(obj, 'Height', None)
            print(f"{obj.Label},{obj.Name},{obj.TypeId},{length},{height}")
            #print(f"Label: {obj.Label:<30} Name: {obj.Name:<20} Type: {obj.TypeId}")
            
