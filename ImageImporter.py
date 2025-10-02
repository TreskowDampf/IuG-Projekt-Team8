

import shutil
import os

#listExtra = open("30-09-2025-AegAllNames.txt", "r")
listExtra = open("ScriptData/TargetImagesNames.txt", "r")

idList = []

# Convert the target filenames into a format which can be compared against 
for id in listExtra.readlines():
    cleanedID = id.split(" ")[0]
    if not cleanedID in idList:
        idList.append(cleanedID)

ImageSubFolders = os.listdir("MuseumImages")
# Check if the MuseumImages folder is empty
if (len(ImageSubFolders) == 0):
    print("Error: The museum image input folder 'MuseumImages' is empty. Please read the ReadMe file.")
    print("Exiting program.")
    quit()

# This folder contains the filenames of all relevant photos
fileNamesAllYears = []

for subFolder in ImageSubFolders:
    fileNamesInSubfolder = os.listdir("MuseumImages/" + subFolder)
    fileNamesAllYears.append(fileNamesInSubfolder)

#print(fileNamesAllYears[0])

fileNameList = []

# An example showing how to correct images are identified
x = "1/1996/7207/000/002.jpg"
y = "1/1996/7207"
if y in x:
    #print("yes")
    pass

for k in fileNamesAllYears:
    for i in k:
        #print(i)
        for j in idList:
            #print(f"{j} vs. {str.replace(i, "-", "/")}")
            if j in str.replace(i, "-", "/"):
                #print(i)
                fileNameList.append(i)

#print(fileNameList)

possibleFilePathsSourceList = []
for fileName in fileNameList:
    for imageSubFolder in ImageSubFolders:
        possibleFilePathsSourceList.append("MuseumImages/" + imageSubFolder + "/" + fileName)
        #print(possibleFilePathsSourceList[0])

#print(possibleFilePathsSourceList)

for possibleFilePathsSource in possibleFilePathsSourceList:
    try:
        shutil.copy(possibleFilePathsSource, "TargetMuseumImages")
        pass
    except Exception as e:
        #print(f"File not found: {y}")#
        #print(e)
        pass

#print(idList)
listExtra.close()
