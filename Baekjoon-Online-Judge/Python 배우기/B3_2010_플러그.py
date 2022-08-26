import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.read().split()))
print(sum(l)-n+1)