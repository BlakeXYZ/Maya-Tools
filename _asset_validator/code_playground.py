import maya.cmds as cmds
import maya.mel as mel
import os


class ValidationError(Exception):
    pass


### RAISE VALIDATION example
# # CHECK if number of selected assets is ONE
# if len(selected_assets) != 1:
#     raise ValidationError(f'Please select only 1 Master Material in Content Browser')





print('hello world')


# List all geometry
list_geo = cmds.ls(geometry=True)
mesh_info = list_geo[0]


# Select the object you want to add the attribute to
selected_object = cmds.ls(selection=True)[0]


def UTILITY_get_asset_name():
    # List all geometry
    list_geo = cmds.ls(geometry=True)
    mesh_info = list_geo[0]

    # Use listRelatives to get the parent of the object
    transform_info = cmds.listRelatives(mesh_info, parent=True)[0]
    asset_name = transform_info

    return asset_name


asset_name = UTILITY_get_asset_name()

    # Use listRelatives to get all shapes under the transform node
mesh_shapes = cmds.listRelatives(asset_name, shapes=True)[0]

print(f'asset_name = {asset_name}')
print(f'mesh_shapes = {mesh_shapes}')





# try:
#     # Add a custom float attribute named "myCustomAttribute"
#     cmds.addAttr(mesh_info, longName="myCustomAttribute", attributeType="float", defaultValue=0.0, keyable=True)
#     print("Custom attribute added successfully!")
# except Exception as e:
#     print(f"Error adding custom attribute: {str(e)}")




# # Name of the string attribute
# string_attribute_name = "Asset_Type"

# # Value to set for the string attribute
# new_string_value = "Hello, World!"


# try:
#     # Add a custom float attribute named "myCustomAttribute"
#     cmds.addAttr(mesh_info, longName=string_attribute_name, dataType="string")
#     print("Custom attribute 02 added successfully!")
# except Exception as e:
#     print(f"Error adding custom attribute 02: {str(e)}")

# try:
#     # Set the default value for the string attribute
#     cmds.setAttr(f"{mesh_info}.{string_attribute_name}", "aaa", type="string")

#     print("setAttr added successfully!")
# except Exception as e:
#     print(f"Error setAttr: {str(e)}")



# try:
#     # Set the value of the custom string attribute
#     cmds.setAttr(f"{mesh_info}.{string_attribute_name}", new_string_value, type="string")
#     print(f"String attribute '{string_attribute_name}' set successfully to: {new_string_value}")
# except Exception as e:
#     print(f"Error setting string attribute: {str(e)}")


# # Use listRelatives to get the parent of the object
# transform_info = cmds.listRelatives(mesh_info, parent=True)

# print(transform_info)

# # List all attributes of 'myCubeShape'
# attributes = cmds.listAttr(transform_info)
# print(attributes)

# object_type = cmds.objectType(mesh_info)
# print('Object Type:', object_type)


# # print(cmds.getAttr(myGeo + '.visibility'))

# # cmds.setAttr(myGeo + '.visibility', True)


# # Get the current scene name
# file_path = cmds.file(q=True, sceneName=True)
# if not file_path:
#     file_path = 'Unsaved Maya Scene!'

# print(f'File Path: {file_path}')

# file_name = file_path.rsplit('/', 1)[-1]

# print(f'File Name: {file_name}')

# print(os.path.splitext(file_name))
