divisor = 3
s = { x for x in range(50)}
print(s)
for i in s:
    if i % divisor == 0:
        print(i)