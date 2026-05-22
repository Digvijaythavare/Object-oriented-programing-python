# to create new directoru using mkdir() function with new directory name
import os
print("Current direcotry : ",os.getcwd())
print()
os.chdir('D:\\')
print("Curretly it has :",os.listdir('D:\\'))


# creating new directory
os.mkdir("Simple1")
print("After creating directory\n")
print(os.listdir())