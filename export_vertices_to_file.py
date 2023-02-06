import bpy


# js's  
imps = ('import { Vector3 } from "three"')
exp_imps = ('export default cylColliders')
arr = ('const cylColliders = [')
arr_e = (']')
vec = ('new Vector3(')
vec_e = ('),')
vec_ef = (')') 

# Open file 
# Set filename before run
f = open("filename", "w")

# write js's
f.writelines(imps + "\n")
f.writelines(arr + "\n")

# Selected object
collider_geo = bpy.context.object

# Data of 
me = collider_geo.data

# for each vertex ...
for v in range(len(me.vertices)):  
    vertices = me.vertices[v].co
    # assemble a string
    vposs = (str(vertices.x) + ',' + str(vertices.y) + ',' + str(vertices.z))    
    if (v == len(me.vertices) - 1):
        f.writelines(vec + vposs + vec_ef + "\n")
    else: 
        f.writelines(vec + vposs + vec_e + "\n")
    
f.writelines(arr_e + "\n")
f.writelines(exp_imps + "\n")   
f.close()