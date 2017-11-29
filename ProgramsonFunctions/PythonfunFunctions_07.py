def length(ob):
    #typecast string to list
    lis=list(ob)

    len=0
    for item in lis:
        len=len+1
    print(len)

s=input("Enter string: ")
length(s)