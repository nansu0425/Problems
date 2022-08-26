n = int(input())
l = list(map(int, input().split()))
c = 0
for i in l:
    b = True
    if i==1:
        b = False
        pass
    for d in range(2, int(i**0.5)+1):
        if i%d==0:
            b = False
            break
    if b:
        c += 1
print(c)