# What the use of it?
When I wanted to know more about the game, I quickly found myself checking each file to see what their type was, and I couldn't continue to do that. So I create this small python script that I will sort each file by their type, so I just needed to look in the folder of the type I wanted to check!

For your information: This script was created in like 1or2 hours, I tried to sort ALL the file from the game, and it worked for me, **but** like everything, their will be bug, don't hesitate to report them =D

# How to use this?
First you need to open the pak folder of the game inside FModel.

Once you have it, you need to click on:

Folders > TheBloodline

You should have a folder named "Content", right click on it, then click on "Save Folder's Packages Properties (.json)", then wait, it will probably take a long time, as the software need to open each assets then export it.

When the software is working on this, you can see at the bottom of it a yellow bar, wait for this bar to be blue with the word "Completed".

Once you got this blue bar, close the software, then open the folder where you have FModel.exe, then you should have a folder:

Output > Exports > TheBloodline > Content

Copy the path that lead you **INSIDE** the content folder, you will need it.

Now open the python script, and at the bottom, you should have:
```python
folder_path = 'C:/Users/YourName/Desktop/Mods Unreal/FModel/Output/Exports/TheBloodline/Content'
```

Edit the line `C:/Users/YourName/Desktop/Mods Unreal/FModel/Output/Exports/TheBloodline/Content` with the path that you copied, **but replace the "\\" by "/" or else the script will not work!!**.

Once you done this, save the script then launch it and wait, you should have a new folder named "SortedFiles" where the "main.py" is, once the script is done, it should close itself, and you can open the new folder, and you should have a lots of folder, each folder = 1 type of assets.

Done!
