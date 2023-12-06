<p align="center">
<img src="https://github.com/BlakeXYZ/Maya-Tools/assets/37947050/d266ef23-06fd-4292-a3e8-1302c3d6826b">
</p>

## <ins>Overview</ins>

<div align="center">
Automate Validations per Asset to enforce standards and ensure consistency amongst team members.
</div>
<br>

<p align="center">  
<img src="https://github.com/BlakeXYZ/Maya-Tools/assets/37947050/b68905a7-a0ab-4905-82cb-b2749777f890" width="700">
</p>


#### Pipeline Problem:
- Having standardized assets is critical to running a clean, collobarative production. As a project evolves and the development team cycles without the support of an automated validator, the risk of an asset library turning into an unorganized, inconsistent library grows. This Tool streamlines the asset validation process, saving time for artists by automating repetitive checks and enforcing consistent standards. 




#### Built with:
- Python 3
- Maya integrated PySide2
- Qt Designer


______
## <ins>Installation</ins>



   1. Download '[Maya-Tools](https://github.com/BlakeXYZ/Maya-Tools/tree/main)' Repo

<p align="center">
<img src="https://github.com/BlakeXYZ/Maya-Tools/assets/37947050/ce521ecd-813e-4bc7-8645-60d330bc19b0" width="700">
</p>

   2. Extract **_asset_validator** Folder
   3. Copy ****_asset_validator**** Folder to:

<p align="center">
<img src="https://github.com/BlakeXYZ/Maya-Tools/assets/37947050/fcca9b3b-5e75-41b7-ac4a-f3d51ef378a4" width="700">
</p>
     
   Windows
```
\Users\USERNAME\Documents\maya\MAYAVERSION\scripts
```
   Linux
```
$HOME/maya/MAYAVERSION/scripts
```
   Mac
```
$HOME/Library/Preferences/Autodesk/maya/MAYAVERSION/scripts
```
   4. Launch / Restart Maya
   5. Inside Script Editor, run:
```py
import os
import sys
import maya.cmds as cmds

# Get the directory where Maya looks for user scripts
maya_scripts_dir = cmds.internalVar(userScriptDir=True)

# Add the asset_validator directory to the Python path
asset_validator_dir = os.path.join(maya_scripts_dir, "_asset_validator")
sys.path.append(asset_validator_dir)

# Import the module
try:
    import mayapy_asset_validator
except ImportError as e:
    print("Import failed:", e)
else:
    # Launch Tool GUI
    mayapy_asset_validator.openWindow()
```
<p align="center">
<img src="https://github.com/BlakeXYZ/Maya-Tools/assets/37947050/84be79e9-2f6d-4003-a321-bfec4fa5340a" width="300">
</p>


____________
## <ins>Quick Start</ins>

#### 🛠️ <em>under construction</em> 🛠️

Describe how to use your tool. Include examples or code snippets to illustrate common use cases. Explain any command-line options, configuration settings, or parameters that users need to be aware of.

______
## <ins>Documentation</ins>

#### 🛠️ <em>under construction</em> 🛠️

Provide a link to more detailed documentation if it exists. This could be a link to a separate documentation file or an external website. Include information on where users can find additional resources, tutorials, or support.


<div align="center">placeholder text.
</div>
<br>

a

<p align="center">
   
<img src="" width="700">
</p>
