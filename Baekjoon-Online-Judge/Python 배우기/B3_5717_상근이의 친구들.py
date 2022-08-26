import sys

while (i := sys.stdin.readline().strip()) != '0 0':
        a, b = map(int, i.split())
        print(a+b)