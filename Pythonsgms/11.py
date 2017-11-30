m1=[[1,2,3],[1,52,23],[16,2,31]]
m2=[[2,3,6],[3,78,20],[3,6,2]]
m3=[[0]*3]*3
for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m1)):
            m3[i][j]+=m1[i][k]*m2[k][j]
print(m3)