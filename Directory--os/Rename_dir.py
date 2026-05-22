# To rename file of directory of file we have rename() function
import os

print("Current Dir :", os.getcwd())

os.chdir('D:\\')
print("Now current dir :", os.getcwd())

os.rename("python", "python3")

print("Folder renamed successfully")