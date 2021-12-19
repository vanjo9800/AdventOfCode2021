#!/usr/bin/env python3

#y1, y2 = (-10,-5)
#x1, x2 = (20,30)
y1, y2 = (-86,-59)
x1, x2 = (209,238)

bestMaxY = 0
cnt = 0
for vx in range(x2+1):
    for vy in range(y1, 500):
        start = (0,0)
        maxY = 0
        tvX, tvY = (vx,vy)
        while start[0] <= x2 and start[1] >= y1:
            maxY = max(maxY, start[1])
            if (start[0] >= x1 and start[0] <= x2) and (start[1] >= y1 and start[1] <= y2):
                bestMaxY = max(bestMaxY, maxY)
                cnt += 1
                break
            start = (start[0] + tvX, start[1] + tvY)
            if tvX > 0:
                tvX -= 1
            elif tvX < 0:
                tvX += 1
            else:
                pass
            tvY -= 1

print(bestMaxY)
print(cnt)
