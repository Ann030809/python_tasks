sp = []
x = 1 
while x != 0:
    x = int(input())
    if x == 0:
        break
    sp.append(x)
print(sum(sp))