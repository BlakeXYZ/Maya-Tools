## Paste this  into Maya Script Editor to load connection:
## commandPort -name "localhost:7001" -sourceType "mel";
## requires MayaCode VSCODE extension

import  os, sys, importlib

print('run')

sys.path.insert(0,'C:\\Users\\blake\\Documents\\PYTHON_Scripting\\2023\\GitHub_Maya_Tools\\Maya-Tools\\_asset_validator')

import importlib 

import mayapy_asset_validator

importlib.reload(mayapy_asset_validator)
mayapy_asset_validator.openWindow() 