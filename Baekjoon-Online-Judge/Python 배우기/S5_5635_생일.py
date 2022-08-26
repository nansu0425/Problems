import sys

n = int(sys.stdin.readline())
l = []
for _ in range(n):
    n, d, m, y = sys.stdin.readline().split()
    l.append([int(y), int(m), int(d), n])
l.sort()
print(l[-1][3], l[0][3], sep='\n')