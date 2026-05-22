import os
import shutil

print("\nInitially it has")
print("Current Dir :", os.getcwd())

os.chdir('D:\\')
print("Now current dir :", os.getcwd())

print(os.listdir())

# Remove empty folder
shutil.rmtree('code')

print(os.listdir())