# Helix Creator

## <ins>Overview</ins>


<div align="center"> 
   
A Simple Tool to Create Helixes. Foundational knowledge thanks to [Isaac Oster](https://isaacoster.gumroad.com/l/oUpTB?layout=profile&recommended_by=library)

</div>

<p align="center">
<img src="https://github.com/BlakeXYZ/Maya-Tools/assets/37947050/1989a23e-d74f-4114-a47f-066bb95905a0" width="900">
</p>

#### Built with:
- Python 3
- Maya integrated PySide2
- Qt Designer

<br>

______
## <ins>Installation</ins>


   1. Download '[Maya-Tools](https://github.com/BlakeXYZ/Maya-Tools/tree/main)' Repo

<p align="center">
<img src="https://github.com/BlakeXYZ/Maya-Tools/assets/37947050/45325716-8ac3-4ed6-a5e6-0bb5f07eecec" width="700">
</p>

   2. Extract **helix_creator.py** File
   3. Copy **helix_creator.py** to:
     
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
try:
    import helix_creator
except ImportError as e:
    print("Import failed:", e)
    
helix_creator.openWindow()
```
<p align="center">
<img src="https://github.com/BlakeXYZ/Maya-Tools/assets/37947050/22b6fd4d-bad7-4729-9c95-d66507228db3" width="300">
</p>

____________
## <ins>Quick Start</ins>

<br>

- Sphere Spread
<p align="center">
<img src="https://github.com/BlakeXYZ/Maya-Tools/assets/37947050/ede8d113-ef9e-4cb3-8d67-7a2d181795df">
</p>
<br>

- Helix Radius

<p align="center">
<img src="https://github.com/BlakeXYZ/Maya-Tools/assets/37947050/ee9a0cbd-ce47-4623-ab08-ce1bf8a3e290">
</p>
<br>

- Helix Spin Speed
  
<p align="center">
<img src="https://github.com/BlakeXYZ/Maya-Tools/assets/37947050/05a0a0c0-8f6d-4ec1-833f-7f06e6407c3a">
</p>
<p align="center">
<img src="https://github.com/BlakeXYZ/Maya-Tools/assets/37947050/6de8f1a1-50c1-436b-8faa-e5c2e6a716c4">
</p>

- Press Play inside the Time Slider to play Expression Editor Animation
<p align="center">
<img src="https://github.com/BlakeXYZ/Maya-Tools/assets/37947050/74408d02-6e81-46db-abda-5043df70b7cf" width="500" >
</p>
<br>
<br>

______
## <ins>Documentation</ins>

- Intelligent Prefix Namespacing

<p align="center">
<img src="https://github.com/BlakeXYZ/Maya-Tools/assets/37947050/da4b0c48-1b6b-4531-88ad-9597477bea76" width="300" >
</p>

```py
    def UTIL_helixGroupPrefix(self):
        # Search for existing 'helix_Group' with a prefix
        existing_groups = cmds.ls('*' + 'helix_Group' + '*', type='transform')

        # Extract the existing prefixes
        existing_prefixes = [group.split('_')[0] for group in existing_groups]

        # If there are no existing groups, start with 'A' as the default
        if not existing_prefixes:
            helixGroupPrefix = 'A'
        else:
            # Sort the existing prefixes
            existing_prefixes.sort()

            # Find the first available letter in the sequence
            for letter in string.ascii_uppercase:
                if letter not in existing_prefixes:
                    helixGroupPrefix = letter
                    break
            else:
                # If all letters are taken, use the next letter after 'Z' ('AA', 'AB', etc.)
                last_prefix = existing_prefixes[-1]
                helixGroupPrefix = string.ascii_uppercase[(string.ascii_uppercase.index(last_prefix) + 1) % 26]

        return(helixGroupPrefix)
```

