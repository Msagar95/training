a=input("Enter numbers: ")
l=a.split()
l[0]=int(l[0])
l[1]=int(l[1])
print("""
Enter operator:-
    1) +
    2) -
    3) *
    4) /
""")
op=input("?")
if op=='1':
    print(l[0]+l[1])
elif op=='2':
    print(l[0]-l[1])
elif op=='3':
    print(l[0]*l[1])
elif op=='4':
    print(l[0]/l[1])
else:
    print("Invalid option")