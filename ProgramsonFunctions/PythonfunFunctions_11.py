def reverse(s):
    rev=''
    for c in s[::-1]:
        rev+=c
    return rev

str=input("Enter the string to be reversed: ")
print("Reversed string:",reverse(str))