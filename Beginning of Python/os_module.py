import os
from datetime import datetime
# getcwd() printing the current Directory
print(os.getcwd())

# changing the current Directory
os.chdir('/home/fahim/Documents/')

print(os.getcwd())

#creating folder in a directory

# using mkdir method
os.mkdir('python-Demo-1')

#using makedirs method
os.makedirs('python-Demo-2/sub-Dir')

#removing Directory from a File system

#rmdir method
os.rmdir('python-Demo-1')

#removedirs method
os.removedirs('python-Demo-2/sub-Dir')

#rename a directory
os.rename('python-Demo-1', 'python-1')

#showing all the file in a Directory
print(os.listdir())

#looking at the file stat

mod_time = os.stat('python').st_atime
print(datetime.fromtimestamp(mod_time))

#walking thorugh all of the directory path, folder and files

for dirpath, dirnames, filenames in os.walk('/home/fahim/Documents/'):
    print('Directory path: ', dirpath)
    print('dirname: ', dirnames)
    print('filename: ', filenames)
    print()

