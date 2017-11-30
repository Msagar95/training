x=[[1,2],[3,4]]
y=[[5,6],[7,8]]
z=[[0,0],[0,0]]
for i in range(0,len(x)):
    for j in range(0,len(x[0])):
        z[i][j]=x[i][j]+y[i][j]
print(z)