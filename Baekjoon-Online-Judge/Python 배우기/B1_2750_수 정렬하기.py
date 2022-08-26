import sys
n = sys.stdin.readline()
sys.stdout.write('\n'.join(map(str, sorted(map(int, sys.stdin.readlines())))))