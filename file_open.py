# Scan dir for files
import os

dir_path = '/home/icadi/Documents/test'
list_dir = os.listdir(dir_path)
file_name = input()

for x in list_dir:
    if x == file_name:
        print(x)
