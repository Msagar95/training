#Creating A List and Accessing by Index:
a=["This","is","a","small","list"]
b=[1,2,3]
c=["word",True,1,2,3]
print(a)
print(b[1])
print(c[1])

#Index Reassignment and .append():
x=[1,2,3]
x[0]=2
x[1]=3
x[2]=4
x.append(6)
print(x)

#List Slicing:
y=[1,2,3,4,5,6,7]
print(y[0:4])
print(y[2:5])
print(y[1:])

#.index() and .insert():
li=["Bob Dylan", "Like a", "Rolling Stone"]
print(li.index("Rolling Stone"))
li.insert(0,"1965")
print(li)

#.remove() and .pop():
a=["McCartney", "Lennon", "Starr", "Harrison", "Sutcliffe"]
a.remove("Sutcliffe")
print(a)
print(a.pop(1))
print(a.pop(2))
print(a)