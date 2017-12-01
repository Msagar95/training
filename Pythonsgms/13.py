punct = "[][!#$%&'()*+,./:;<=>?@\^_`{|}~-]"
s=input("Input string: ")
ans=""
for c in s:
    if c not in punct:
        ans+=c
print(ans)