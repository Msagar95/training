interval = input("Enter interval: ")
li=interval.split()
n1,n2=int(li[0]),int(li[1])
print(n1,n2)

def arm_check(n):
    temp=n
    sum=0
    while int(n)>0:
        x=n%10
        sum += x**3
        n//=10
    if temp == sum:
        return True
    else:
        return False
for i in range(n1,n2):
    if arm_check(i):
        print(i, "is an Armstrong number")