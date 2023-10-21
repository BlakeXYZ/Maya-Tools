### 
# Isaac Oster's - "Introduction to Python Scripting in Maya" course
###

from maya import cmds as mc

print("_______________\n")

################################
## Cube of Spheres

# mc.sphere(r=5, ssw=0, esw=180)
# mc.move(0, 0, -10, r=True)


# for i in range (0,5):
#    for j in range (0,5):
#       for k in range (0,5):

#         mc.sphere(r=0.5)
#         mc.move(i, j*2, k, r=True) 


################################
## Get Selection

# mySelection = mc.ls(selection = True)

# print(f'my selection {mySelection}')


################################
## Circle of Cones
## Animating with Expressions

# import math

# rotateAngle = 0
# for i in range(0,20):
        
#     # Create a polygonal cone
#     cone = mc.polyCone()[0] # Get the first item from the list, which is the cone's name

#     # Move the cone up by 10 units along the Y-axis
#     mc.move(0, 0, 10, cone, relative=True)

#     # Move the pivot point to the base of the cone (bottom center)
#     mc.move(0, 0, -10, cone + '.scalePivot', cone + '.rotatePivot', relative=True)

#     # Rotate the cone 5 degrees around the Y-axis
#     mc.rotate(0, rotateAngle, 0, cone, relative=True)

#     # yTranslate = math.sin(math.radians(rotateAngle))
#     # mc.move(0, yTranslate, 0, cone,  relative=True)

#     expressionString = f'{cone}.translateY = sin(time*2+{rotateAngle});'
#     mc.expression(string=expressionString, object=cone, ae=True, uc='all')

#     rotateAngle += 18
#     # print(rotateAngle)

################################
## Randomly Place Spheres

# import random

# for i in range(1):
#     randX = random.randint(-10,10)
#     randZ = random.randint(-10,10)


#     mc.polySphere() 
#     mc.move(randX, 0 , randZ)

################################
## Assign Vertex Color
# import math


# rotateAngle = 0

# for i in range(0,30):

#     # Create mySphere
#     mySphere = mc.polySphere(r=1)[0] 

#     # Move mySphere
#     mc.move(0,0,10, r = True)

#     # Move mySphere Pivot Back to Origin
#     mc.move(0,0,-10, mySphere + '.scalePivot', mySphere + '.rotatePivot',  r = True)

#     # Rotate mySphere by rotateAngle
#     mc.rotate(0, rotateAngle, 0, mySphere,  r = True)

#     # Set RGB vertex color values
#     redVal = math.sin(math.radians(i * 12 ))
#     greenVal = math.sin(math.radians(i * 12 + 120))
#     blueVal = math.sin(math.radians(i * 12  + 240))
#     # Convert from -1,1 to 0,1 range
#     redVal = (redVal + 1) / 2
#     greenVal = (greenVal + 1) / 2
#     blueVal = (blueVal + 1) / 2

#     print(f"Red: {redVal}, Green: {greenVal}, Blue: {blueVal}")

#     # Apply Poly Color
#     mc.polyColorPerVertex(rgb=(redVal,greenVal,blueVal), cdo = True)

#     rotateAngle += 12

################################
## Get and Set Attributes

# mc.shadingNode('distanceBetween', asUtility = True )

# mc.connectAttr('pSphere1.translate', 'distanceBetween1.point1', f = True)
# mc.connectAttr('pSphere2.translate', 'distanceBetween1.point2', f = True)


# print(mc.getAttr('distanceBetween1.distance'))

################################
## Spheres That Don't Touch

# import random

# totalSphereCount = 10
# storedSpheres = []

# # Build Base Sphere
# randX = random.uniform(-10,10)
# randZ = random.uniform(-10,10)
# mySphere = mc.polySphere(name = 'mySphere0')[0]
# mc.move(randX,0,randZ)

# storedSpheres.append(mySphere)


# # Build distanceBetween Utility Node For Comparison Loop
# if mc.objExists('myDistanceNode'):
#     print('myDistanceNode Already Exists!')
# else:
#     mc.shadingNode('distanceBetween', asUtility = True, name='myDistanceNode' )
#     print('myDistanceNode Has Been Created')


# for currentSphere in range(1, totalSphereCount):
#     print(storedSpheres)
#     randX = random.uniform(-10,10)
#     randZ = random.uniform(-10,10)

#     currentSphere = mc.polySphere(name = 'currentSphere')[0]
#     mc.move(randX,0,randZ)

#     # Comparing currentSphere to storedSphere distance, remove if too close
#     should_delete = False
#     print(f' ------ comparing {currentSphere}')
#     for storedSphere in storedSpheres:

#         mc.connectAttr(currentSphere + '.translate', 'myDistanceNode.point1', f = True)
#         mc.connectAttr(storedSphere + '.translate', 'myDistanceNode.point2', f = True)

#         sphereDistance = mc.getAttr('myDistanceNode.distance')
#         print(f'{currentSphere} and {storedSphere} distance = {sphereDistance}')

#         mc.disconnectAttr(currentSphere + '.translate', 'myDistanceNode.point1')
#         mc.disconnectAttr(storedSphere + '.translate', 'myDistanceNode.point2')

#         if sphereDistance < 2:
#             print(f'oh no {currentSphere} < 2 distance = {sphereDistance}')
#             should_delete = True
#             continue
#     if should_delete:
#         print(f'Now Deleting {currentSphere}')
#         mc.delete()
#         continue

#     rename = 'mySphere' + str(len(storedSpheres))
#     mc.rename('currentSphere', rename)
#     storedSpheres.append(rename)


################################
## Spinning Torus

# import random
# import math

# groupCount = 36

# for currentGroup in range(groupCount):

#     sphereA = 'sphere_a_' + str(currentGroup)
#     sphereB = 'sphere_b_' + str(currentGroup)
#     sphereC = 'sphere_c_' + str(currentGroup)
#     radius = 2

#     mc.polySphere(name = sphereA)[0]
#     mc.move(radius,0,0)

#     mc.polySphere(name = sphereB, r=.75)[0]
#     mc.rotate(0,120,0, r=True, os=True)
#     mc.move(radius,0,0, r=True, os=True, wd=True)

#     mc.polySphere(name = sphereC, r=.5)[0]
#     mc.rotate(0,240,0, r=True, os=True)
#     mc.move(radius,0,0, r=True, os=True, wd=True)

#     # Animate polySpheres

#     # Create Parent Group
#     mc.select(d=True)   
#     parentGroupName = 'group_' + str(currentGroup)
#     mc.group(name = parentGroupName, em=True)
#     mc.parent(sphereA, sphereB, sphereC, parentGroupName)

#     # Rotate Parent Group
#     mc.select(parentGroupName)   
#     mc.rotate(0,(40 * currentGroup),0, r=True, ws=True)
#     mc.makeIdentity(apply=True, r=True)

#     # Move Parent Group
#     mc.move(10,0,0, r=True, os=True, wd=True)

#     # Animate Parent Group
#     expressionString = f'{parentGroupName}.rotateY = time * 35;'
#     mc.expression(string=expressionString, object=parentGroupName, ae=True, uc='all')

#     # Create Grandparent Group
#     mc.select(d=True)   
#     grandparentGroupName = 'grandgroup_' + str(currentGroup)
#     mc.group(name = grandparentGroupName, em=True)
#     mc.parent(parentGroupName, grandparentGroupName)

#     # Rotate Grandparent Group
#     mc.select(grandparentGroupName)   
#     mc.rotate(0,0,(10 * currentGroup), r=True, ws=True)

#     # Set RGB vertex color values
#     mc.select(d=True)   
#     mc.select(sphereA, sphereB, sphereC)
#     redVal = math.sin(math.radians(currentGroup * 12 ))
#     greenVal = math.sin(math.radians(currentGroup * 12 + 120))
#     blueVal = math.sin(math.radians(currentGroup * 12  + 240))
#     # Convert from -1,1 to 0,1 range
#     redVal = (redVal + 1) / 2
#     greenVal = (greenVal + 1) / 2
#     blueVal = (blueVal + 1) / 2
#     # Apply Poly Color
#     mc.polyColorPerVertex(rgb=(redVal,greenVal,blueVal), cdo = True)































