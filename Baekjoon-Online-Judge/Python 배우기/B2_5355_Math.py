import sys

for _ in range(int(input())):
    data_set = sys.stdin.readline().split()
    num = float(data_set[0])
    
    for it in data_set[1:]:
        if it=='@':
            num *= 3
        elif it=='%':
            num += 5
        elif it=='#':
            num -= 7
    
    print(format(num, '.2f'))