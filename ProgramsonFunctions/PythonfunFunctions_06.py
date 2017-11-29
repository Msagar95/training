def max_of_three(a,b,c):
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))

print("Maximum of three=",max_of_three(a,b,c))