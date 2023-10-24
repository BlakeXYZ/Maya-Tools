import maya.cmds as cmds
import os
import inspect

# Get the directory where userSetup.py is located

script_directory = os.path.dirname(inspect.getfile(inspect.currentframe()))
yourDailyFunFact_path = script_directory + "/yourDailyFunFact.py"

# Create a script job that runs the external script on sceneOpened event
scriptJobID = cmds.scriptJob(e=["SceneOpened", lambda script_directory=script_directory: exec(open(yourDailyFunFact_path).read(), globals())])



# Define a function to run an external script
# def runScript(yourDailyFunFact_path):
#     try:
#         with open(yourDailyFunFact_path, 'r') as file:
#             script_contents = file.read()
#             exec(script_contents, globals())
#     except Exception as e:
#         print("Error running script:", str(e))





