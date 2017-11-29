def translate(s):
    ind=0
    for c in s:
        ind=ind+1
        if c in "qwrtypsdfghjklzxcvbnm":
            s=s[:ind]+'o'+c+s[ind:]
            ind=ind+2
    return s

str=input("Enter the string to be translated: ")
print(translate(str))