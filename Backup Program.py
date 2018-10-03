#Program takes files from multiple locations and sorts them by extension.
#It will also see if any changes have been made to already backup files.

import os, shutil, time

Name = ["""Directories, to, backup"""]
index = 0
os.chdir("""Directory to store Backups""")

while index < len(Name):
    for folderName, subfolders, filenames in os.walk(Name[index]):
        for filename in filenames:
            name, ext = os.path.splitext(filename)
            ext = ext[1:]
            Dest = """Directory to store Backups""" + ext
            if os.path.exists(Dest):
                pass
            else:
                #Creates folders in destination to store different file extensions
                os.mkdir(ext)
            currentPath = os.path.join(folderName, filename)
            futurePath = Dest + '\\'+ filename
            if os.path.exists(futurePath):
                if os.path.getmtime(futurePath) == os.path.getmtime(currentPath):
                    #Checks metadata to see if source files have been changed
                    pass
                else:
                    #Creates paths for renamed files to be stored
                    ext = '.' + ext
                    newName = (name + ' ' + time.ctime(os.path.getmtime(futurePath)) + ext).replace(':','_')
                    renamedPath = ("""Directory to store Temp Backups""" + newName).replace('\u202a','')
                    renamedDest = Dest + '\\' + newName
                    if os.path.exists(renamedDest):
                        pass
                    else:
                        print(renamedPath)
                        #Copies files to temp location
                        shutil.copy2 (currentPath, """Directory to store Temp Backups""")
                        #Renames files in temp location
                        os.rename("""Directory to store Temp Backups""" + filename, renamedPath)
                        #Copies files final destination
                        shutil.copy2 (renamedPath,Dest)
                        #Deletes temp files
                        os.remove(renamedPath)
            else:
                #Copies files that are not in the Destination
                print(currentPath)
                shutil.copy2 (currentPath,Dest)
    index += 1
