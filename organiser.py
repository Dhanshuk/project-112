from fileinput import filename
import os
import shutil

to_dir  = "C:/Users/Dhanshuk Ashish/OneDrive/Pictures/Screenshots"
from_dir = "C:/Users/Dhanshuk Ashish/OneDrive/Desktop/screenshots"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:

    name,extension = os.path.splitext(file_name)

    if extension == '':
        continue

    if extension in ['.doc','.pdf','.txt','.wps','.xml']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "pdf_file"
        path3 = to_dir + '/' + "pdf_file" + '/' + file_name

        if os.path.exists(path2):
            print("moving " + file_name + ".......")

    else:
        os.makedirs(path2)
        print("moving " + file_name + ".......")
        shutil.move(path1,path3)        