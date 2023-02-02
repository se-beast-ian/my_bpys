import bpy

# Selected Object
collider = bpy.context.object

# Collect data 
me = collider.data

# For each vertex in the range of vertices, print the coordinates
for v in range(len(me.vertices)): 
    print(me.vertices[v].co)
  