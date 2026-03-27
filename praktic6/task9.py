st = input()
a = len(st)

if a % 2 == 0 :
    a = int(len(st)/ 2) 
    print(st[a::] + st[:a:])
else:
    a = (a//2) + 1
    print(st[a::] + st[:a:])