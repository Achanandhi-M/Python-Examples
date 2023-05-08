import os

if os.path.exists('file.txt'):
    os.remove('file.txt')
    print('File is deleted')

else:
    print('File does not exist')
