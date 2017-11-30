import os
li=[]
path = "C:/Users/sagmukhe/PycharmProjects/training/Textfiles"
os.chdir(path)
dirs = os.listdir( path )
for file in dirs:
   li.append(file)
li.append("bogus.txt")

for fil in li:
   try:
       file_object = open(fil, 'r+')
       x=str(file_object.read())
       x=(str(x).split())
       print(fil,x[1])
       file_object.close()
   except FileNotFoundError:
       print(fil,"not found")