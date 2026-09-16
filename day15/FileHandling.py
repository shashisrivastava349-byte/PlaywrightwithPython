#Example 1: Create/writing a file
#Approach 1: 'w' represents write
# file=open("D:\\Playwright_Python_Notes\\myfile.txt",'w')
# file.write("Welcome to file Handling \n Python File Handling")
# file.close()

#Approach 2: 'a' represents Appending
# with open("D:\\Playwright_Python_Notes\\myfile.txt",'w')as file:
#     file.write("Welcome to file Handling \n Python File Handling")
#     file.close()

#Example 2: Appending data into file
# file=open("D:\\Playwright_Python_Notes\\myfile.txt",'a')
# file.write("\n This line is Appended \n File Handling")
# file.close()

#Example 3: Reading data from text file 'r' represent Reading file
# read() - reads entire data
# readline() - read single line
# readlines() - read all the lines in list format

# file=open("D:\\Playwright_Python_Notes\\myfile.txt",'r')
# # contentinFile=file.read()
# # contentinFile=file.readline()
# contentinFile=file.readlines()
# print(contentinFile)
# file.close()

#Example 4: Renaming the file
# import os
# os.rename("D:\\Playwright_Python_Notes\\myfile.txt", "D:\\Playwright_Python_Notes\\myfile1.txt")
# print("File renamed")

#Example 5: Deleting the File
# import os
# file="D:\\Playwright_Python_Notes\\myfile1.txt"
# if os.path.exists(file):
#     os.remove(file)
# else:
#     print("file does not exist")

#Example 6: Creating a directory/folder
# import os
# os.mkdir("D:\\Playwright_Python_Notes\\mydirectory")
# print("Directory Created...")

#Example 7: Check directory/folder exist or not
# import os
# mydir="D:\\Playwright_Python_Notes\\mydirectory"
# if os.path.exists(mydir):
#     print("Directory exists")
# else:
#     print("Directory does not exist")

#Example 8: Rename directory/folder
# import os
# os.rename("D:\\Playwright_Python_Notes\\mydirectory","D:\\Playwright_Python_Notes\\mydirectoryRenamed")
# print("Directory Renamed")

#Example 9: Remove the directory
# import os
# import shutil
# os.rmdir("D:\\Playwright_Python_Notes\\mydirectoryRenamed") #if folder is empty
#shutil.rmtree("D:\\Playwright_Python_Notes\\mydirectoryRenamed") #if folder contains files

#Example 10: Get the current working directory
import os
print(os.getcwd())









