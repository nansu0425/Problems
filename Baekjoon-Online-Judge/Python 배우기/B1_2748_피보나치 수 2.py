n = int(input())
fb = [0, 1]
if n==1:
    print(1)
else:
    for _ in range(2, n+1):
        fb.append(fb[-1]+fb[-2])
    print(fb[-1])