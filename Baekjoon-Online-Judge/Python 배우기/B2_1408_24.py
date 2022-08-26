pt = input()
st = input()
pts = int(pt[0:2])*3600 + int(pt[3:5])*60 + int(pt[6:8])
sts = int(st[0:2])*3600 + int(st[3:5])*60 + int(st[6:8])
if pts>sts:
    rts = sts+(24*3600) - pts
else:
    rts = sts - pts
print("{0:02d}:{1:02d}:{2:02d}".format(rts//3600, rts%3600//60, rts%3600%60))