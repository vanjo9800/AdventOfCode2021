#!/usr/bin/env python3

f = open("puzzle_test.txt","r")
f = open("puzzle.txt","r")
lines = f.readlines()

commands = []

def execute(code,z,w,x,y):
    val = {}
    val['w'] = w
    val['z'] = z
    val['x'] = x
    val['y'] = y
    for line in code:
        cmd,x,y = line.split(" ")
        if y[-1].isdigit():
            y=int(y)
        if cmd == 'add':
            if type(y) == int:
                val[x] += y
            else:
                val[x] += val[y]
        if cmd == 'mul':
            if type(y) == int:
                val[x] *= y
            else:
                val[x] *= val[y]
        if cmd == 'div':
            if type(y) == int:
                val[x] //= y
            else:
                val[x] //= val[y]
        if cmd == 'mod':
            if type(y) == int:
                val[x] %= y
            else:
                val[x] %= val[y]
        if cmd == 'eql':
            if type(y) == int:
                if val[x] == y:
                    val[x] = 1
                else:
                    val[x] = 0
            else:
                if val[x] == val[y]:
                    val[x] = 1
                else:
                    val[x] = 0
    return val['z']

for i in range(len(lines)):
    lines[i] = lines[i][:-1]
    line = lines[i]
    if line[:3] == 'inp':
        commands.append(i)
commands.append(len(lines))

# last = {}
# last[0] = ''
# lastP = len(lines)
# for c in range(len(commands)-1)[::-1]:
#     newLast = {}
#     for d in range(1,10):
#         for z in range(-1000,1001):
#             resZ = execute(lines[commands[c]+1:lastP],z,d,0,0)
#             if resZ in last:
#                 newLast[z] = str(d) + last[resZ]
#     #print(''.join(lines[commands[c]:lastP+1]))
#     last = newLast
#     #print(c,len(last.keys()))
#     #print(last)
#     lastP = commands[c]

startZ = []
startZ.append([0])
#digs = '94992994195998'
digs =  '21191861151161'
z = 0
for c in range(len(commands)-1):
    nz = execute(lines[commands[c]+1:commands[c+1]],z,int(digs[c]),0,0)
    print(nz)
    z = nz

#print(last)
