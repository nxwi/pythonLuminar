import os

print(os.getcwd())

# Create a directory.
os.mkdir(r'/Users/naswih/PycharmProjects/pythonProject/modules/builtIn/newDir')

# Create user input directory.
# path = input("Enter the directory name:")
# os.mkdir(f'/Users/naswih/PycharmProjects/pythonProject/{path}')
# print('done')

# Return a list containing the names of the files in the directory.
print(os.listdir('/Users/naswih/PycharmProjects/pythonProject/modules/builtIn'))

# Remove a directory.
os.rmdir('/Users/naswih/PycharmProjects/pythonProject/modules/builtIn/newDir')

# Remove a file.
os.remove('/Users/naswih/PycharmProjects/pythonProject/modules/builtIn/temp.py')

import shutil

shutil.rmtree('/Users/naswih/Downloads/LinkedIn copy')
