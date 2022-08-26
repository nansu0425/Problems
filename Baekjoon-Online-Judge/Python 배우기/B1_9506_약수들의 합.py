import sys

while (n := int(sys.stdin.readline())) != -1:
    fl = [1]
    for d in range(2, int(n**0.5)+1):
        if n%d==0:
            fl.extend([d, n//d])
    if n==sum(fl):
        fls = ' + '.join(map(str, sorted(fl)))
        print("%d = %s"%(n, fls))
    else:
        print("%d is NOT perfect."%n)