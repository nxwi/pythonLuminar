import os

print(os.getcwd())

# Create a directory.
os.mkdir(r'/main/modules/builtIn/newDir')

# Create user input directory.
# path = input("Enter the directory name:")
# os.mkdir(f'/Users/naswih/PycharmProjects/pythonProject/{path}')
# print('done')

# Return a list containing the names of the files in the directory.
print(os.listdir('/main/modules/builtIn'))

# Remove a directory.
os.rmdir('/main/modules/builtIn/newDir')

# Remove a file.
os.remove('/main/modules/builtIn/temp.py')

import shutil

shutil.rmtree('/Users/naswih/Downloads/LinkedIn copy')
