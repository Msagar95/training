s=input("Calculate: ")
def calc(s):
    l=s.split()
    l[0]=int(l[0])
    l[2]=int(l[2])
    if l[1] == '+':
        print(l[0] + l[2])
    elif l[1] == '-':
        print(l[0] - l[2])
    elif l[1] == '*':
        print(l[0] * l[2])
    elif l[1] == '/':
        print(l[0] / l[2])
calc(s)