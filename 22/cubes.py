#!/usr/bin/env python3

import re

# f = open("puzzle_simple.txt","r")
# f = open("puzzle_test.txt","r")
f = open("puzzle.txt","r")
lines = f.readlines()

byX = []

def keyTuple(x):
    return x[0]

for i in range(len(lines)):
    line = lines[i]
    status, command = line[:-1].split(' ')
    x_int, y_int, z_int = command.split(',')
    x = [int(s) for s in re.findall(r'-?\d+', x_int)]
    y = [int(s) for s in re.findall(r'-?\d+', y_int)]
    z = [int(s) for s in re.findall(r'-?\d+', z_int)]

    byX.append((x[0], (y,z,i,status), 1))
    byX.append((x[1]+1, (y,z,i,status), 0))

ans = 0
byX.sort(key=keyTuple)
stack = []
for i in range(len(byX)-1):
    xSpan = byX[i+1][0] - byX[i][0]
    if byX[i][2] == 1:
        stack.append(byX[i][1])
    else:
        stack.pop(stack.index(byX[i][1]))
    
    byY = []
    for r in stack:
        byY.append((r[0][0],(r[1],r[2],r[3]), 1))
        byY.append((r[0][1]+1,(r[1],r[2],r[3]), 0))
    byY.sort(key=keyTuple)

    yStack = []
    for j in range(len(byY)-1):
        ySpan = byY[j+1][0] - byY[j][0]
        if byY[j][2] == 1:
            yStack.append(byY[j][1])
        else:
            yStack.pop(yStack.index(byY[j][1]))

        byZ = []
        for r in yStack:
            byZ.append((r[0][0],(r[1],r[2]),1))
            byZ.append((r[0][1]+1,(r[1],r[2]),0))
        byZ.sort(key=keyTuple)

        zStack = []
        for k in range(len(byZ) - 1):
            zSpan = byZ[k+1][0] - byZ[k][0]
            if byZ[k][2] == 1:
                zStack.append(byZ[k][1])
            else:
                zStack.pop(zStack.index(byZ[k][1]))

            if len(zStack) > 0 and sorted(zStack,key=keyTuple, reverse=True)[0][1] == 'on':
                ans += xSpan * ySpan * zSpan
print(ans)


