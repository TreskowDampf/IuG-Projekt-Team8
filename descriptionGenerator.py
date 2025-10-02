"""
Tutorial for running from CLI: https://www.hostinger.com/tutorials/ollama-cli-tutorial 

 The script requires the following to run:
 - ollama installed on system (check by running 'ollama --version' in Command Line)
 - The model gemma3:27b installed on system (check by running 'ollama list')
 - 
"""

import os
import xlsxwriter
#import ollama

#testString = "1-2024-0733-000-001"
#print(testString[:15])

def saveOutputToExcel(imageNameArray, valueArray):
    workbook = xlsxwriter.Workbook('ScriptData/ScriptOutput.xlsx')
    worksheet = workbook.add_worksheet('Output')

    # iterate through arrays and write for each line
    for row in range(1, len(imageNameArray)+1):

        worksheet.write("A" + str(row), imageNameArray[row-1])
        worksheet.write("B" + str(row), valueArray[row-1])

    workbook.close()

#saveOutputToExcel(["Test1", "Test2", "Test3"], ["TestA", "TestB", "TestC"])
#quit()

imageNames = os.listdir("TargetMuseumImages")

#dir = os.system("dir")

# Start ollama
#os.system(f"ollama run gemma3:27b")

# group images by object (each object has about 6 images to show it from all angles)
# for example: 1-2024-0733-000-001 should be split into 1-2024-0733-000.

objectSubArrayArrays = [] # This array contains subArrays that contain images showing the same object
# will look like this "[[1-1, 1-2, 1-3], [2-1, 2-2, 2-3], [3-1, 3-2, 3-3]]"


# group all images showing the same object using arrays
sameImageArrayArray = []
for imageName in imageNames:
    
    # check if the image was already checked once
    alreadyFound = False
    for array in sameImageArrayArray:
        for imageName2 in array:
            if imageName == imageName2:
                alreadyFound = True
                break
        if alreadyFound:
            break

    if not alreadyFound:
        # find all images showing the same object
        sameImageArray = []
        for imageNameCompare in imageNames:
            if imageName == imageNameCompare:
                sameImageArray.append(imageNameCompare)
                pass

            elif imageName[:15] == imageNameCompare[:15]:
                # new image of same object found, adding to array
                sameImageArray.append(imageNameCompare)
        
        #print(sameImageArray)
        sameImageArrayArray.append(sameImageArray)
    
    #quit()

# Due to xlsxwriter library limitations, appending to the excel document is not possible.
# Therefore, the entire list always needs to be rewritten to excel
OutputExcelColumn1 = []
OutputExcelColumn2 = []
for sameObjectArray in sameImageArrayArray:
    
    locationString = ""
    for image in sameObjectArray:
        locationString = locationString + f'"./TargetMuseumImages/{image}", '

    descriptionPrompt = f"""Please describe the object in the images at the following locations: {locationString}".
    They are all the same object, write a single description. Keep it as short as possible.
    """

    #print(descriptionPrompt)
    #quit()

    inputPrompt = f'ollama run gemma3:27b "{descriptionPrompt}"'
    print(inputPrompt)

    response = os.system(f"{inputPrompt}")

    OutputExcelColumn1.append(sameObjectArray[0])
    OutputExcelColumn2.append(response)
    saveOutputToExcel(OutputExcelColumn1, OutputExcelColumn2)

    quit()

