import sys

l = [int(sys.stdin.readline()) for _ in range(10)]
print(sum(l)//len(l), max(l, key=l.count), sep='\n')