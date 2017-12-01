X = [[12,7,3],[4 ,5,6],[7 ,8,9]]
Y = [[5,8,1],[6,7,3],[4,5,9]]
Z = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           Z[i][j] += X[i][k] * Y[k][j]
print(Z)