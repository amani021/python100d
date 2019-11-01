#-------- DAY 69 "file handling" --------
import os
print("Lesson 69: File Handling")
# 1. Open a File: syntax: f = open("FileName", "Mode")
# 2. Read Files
# 3. Close Files
# 4. Write to a File
# 5. Create a New File
# 6. Delete a File
# 7. Delete a Folder
# * Mode:
#     a. "x": Create a new empty file, *** NOTE: raise an error if it exist !!***
#     b. "w": Overwrite any existing content on a file
#     c. "a": Append (continue write) to the end of a file
#     - b & c: Will open new file if it doesn't exist
#     d. "r": (Default value), open a file for reading, *** NOTE: raise an error if it doesn't exist !!***
f = open("myFile.txt", "x")
f.write("Hello, this lesson is for dealing with files\n Let's go to try!")
f.close() #Should always close to save

f = open("myFile.txt", "r")
print("Read the file:\n", f.read()) #Read all contents on the file
f.close()

f = open("myFile.txt", "r")
print("---------------------\nRead a part of the file:\n", f.read(5)) #read(Number of Character)
f.close()

f = open("myFile.txt", "r")
print("---------------------\nRead a line:\n", f.readline()) #If you want to read more than one line, you'll repeat readline()
f.close()

f = open("myFile.txt", "a")
f.write("\n Woops! I'm very late!\n")
f.close()

f = open("myFile.txt", "r")
print("---------------------\nAfter appending:")
for x in f:
    print("", x) #Read line by line (whole lines in the file)

#Check if the file exist or not before delete it
# if os.path.exists("myFile.txt"):
#     os.remove("myFile.txt")
# else:
#     print("The file doesn't exist!")

#Only delete an empty folder
# os.rmdir("codes")
