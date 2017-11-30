n=int(input("Enter no: "))
m=0
while int(n)>0:
    m*=10
    m +=int(n%2)
    n/=2
print(m)