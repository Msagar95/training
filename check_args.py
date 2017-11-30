import sys
args=(sys.argv)[1:]

try:
    args[0]=int(args[0])
    print("1st-success")
except ValueError:
    print("First arguement isn't integer")

try:
    args[1]=float(args[1])
    print("2nd-success")
except ValueError:
    print("Second arguement isn't float")