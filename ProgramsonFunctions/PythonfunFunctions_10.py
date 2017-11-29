def sum(l):
    s=0
    for it in l:
        s=s+it
    return s

def multiply(l):
    m=1
    for it in l:
        m=m*it
    return m

print(sum([1,2,3,4]))
print(multiply([1,2,3,4]))