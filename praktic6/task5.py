st = input()
a = 0
for i in range(len(st)-1):
    if st[i] == st[i+1]:
        a += 1 
print(a)