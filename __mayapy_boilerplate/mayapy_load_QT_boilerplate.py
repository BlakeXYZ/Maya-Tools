## Paste this  into Maya Script Editor to load connection:
## commandPort -name "localhost:7001" -sourceType "mel";
## requires MayaCode VSCODE extension

import  os, sys, importlib

print('run')

sys.path.insert(0,'C:\\Users\\blake\\Documents\\PYTHON_Scripting\\2023\\GitHub_Maya_Tools\\Maya-Tools\\__mayapy_boilerplate')

import importlib 

import mayapy_QT_boilerplate

importlib.reload(mayapy_QT_boilerplate)
mayapy_QT_boilerplate.openWindow()

