import sys
file=sys.argv[1]
print(file)

try:
    file_object=open(file,'r+')
    print("File successfully opened")
except FileNotFoundError:
    print("File doesn't exist")
except IOError:
    print("Couldn't read the file properly")