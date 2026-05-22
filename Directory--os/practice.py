# Now we are creating a directory and then removing it using the os module functions
import os
import time
def Create_file_ane_folder():
    print("Current direcotry :  ",os.getcwd())
    print("Change direcotry :",os.chdir('D:\\'))
    time.sleep(3)
    Folder_name = input("Enter the foler name to create : ")

    if not os.path.exists(Folder_name):
        os.mkdir(Folder_name)
        print(f"Folder {Folder_name} created successfully ✅")
    else:
        print(f"Folder {Folder_name} already exists.")

    time.sleep(3)   
    
    File_name = input("Enter the file name to create :")

    file_path = os.path.join(Folder_name,File_name)

    if not os.path.exists(file_path):
        with open(file_path,'w') as f:
            f.write("This is a sample file ")
        print(f"File {File_name} created successfully in folder {Folder_name} ✅")
    else:
        print(f"File {File_name} already exists in folder {Folder_name}.")        

Create_file_ane_folder()       