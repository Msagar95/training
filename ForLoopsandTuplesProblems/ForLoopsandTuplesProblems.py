#Tuples:
x=3.14,1,True,"word"
print(x)
print(x[1])
print(x[0])
print(x[:3])
print(x[-3:])
print(x[1:3])

#For Loops:
a=("Bohr", "Leibniz", "Einstein")
b=[]
c=[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for i in range(len(a)):
    print(a[i])
for i in range(2,8):
    b.append(c[i])
print(b)