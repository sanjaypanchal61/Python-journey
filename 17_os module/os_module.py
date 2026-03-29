# import os module
import os

# current directory
print(os.getcwd())

# list files
print(os.listdir())

# create folder
os.mkdir('demo')

# remove folder
os.rmdir('demo')

# check file exists
print(os.path.exists("file.txt"))

# join path
os.path.join('folder_name','file_name')