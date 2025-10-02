Welcome to the AI Powered Museum Object Description Generator (AIPMODG)
Created by Team 8
01.10.2025
===========================================
Table of Contents:
1. Requirements
2. Quick Startup
3. Scripts included
4. Processes described

===========================================
1. Requirements

1. Ollama installed on the system
2. The model "gemma3:27b" should be installed through Ollama
3. Using PIP, install the library "xlsxwriter"

===========================================
2. Quick Startup

Note: This guide assumes you have access to images of museum objects, and have a range of filenames you
would like to download available as a text document.

1. Download the project into a location that does not require admin privileges to access
2. Download the museums objects into the folder "/MuseumImages". Make sure the Museum Images are sorted into
   years by folders. The MuseumImages folder should for example now contain folders named "1996", "1997", etc.
3. Clear the .txt document "TargetImageNames" in the folder "ScriptData"
4. Clear the folder "TargetMuseumImages"
5. Clear the excel file "ScriptOutput" at the file location "ScriptData". All cells should be empty.
6. Paste all filenames of images you would like to write descriptions for into the the .txt document "TargetImageNames"
   in the folder "ScriptData"
7. Open a command line interface and navigate to the folder "ProjectMasterFolder"
8. Run the Command "Python descriptionGenerator.py"