import os
import shutil

folder_path = input("Enter folder path: ")
new_folder = input("Enter the name of the new folder: ")

try:
    os.mkdir(os.path.join(folder_path, new_folder))
except:
    print("Error: folder already exists.")

for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        ext = os.path.splitext(filename)[1][1:]
        if not os.path.exists(os.path.join(folder_path, new_folder, ext)):
            os.mkdir(os.path.join(folder_path, new_folder, ext))
        shutil.move(os.path.join(folder_path, filename), os.path.join(folder_path, new_folder, ext))
