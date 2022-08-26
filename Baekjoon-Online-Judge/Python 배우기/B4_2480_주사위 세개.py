l = sorted(list(map(int, input().split())))
sl = len(set(l))
if sl==1: 
    print(10000+l[0]*1000)
elif sl==2:
    print(1000+l[1]*100)
else:
    print(l[2]*100)
    