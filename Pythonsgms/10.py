x=[[1,2],[3,4]]
y=[[0,0],[0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        y[i][j]=x[j][i]
x=y
print(x)