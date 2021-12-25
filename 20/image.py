#!/usr/bin/env python3

# f = open("puzzle_test.txt","r")
f = open("puzzle.txt","r")
lines = f.readlines()

algorithm = lines[0]
def trim_newline(l):
    return l[:-1]
input_image = list(map(trim_newline,lines[2:]))

flag = False
def numX(map,i,j):
    global flag

    ans = 0
    for dx in (-1,0,1):
        for dy in (-1,0,1):
            ans *= 2
            if flag:
                ans += 1
            if i+dx >= 0 and i+dx < len(map):
                if j+dy >=0 and j+dy < len(map[0]):
                    if flag:
                        if map[i+dx][j+dy] == '.':
                            ans -=1
                    else:
                        if map[i+dx][j+dy] == '#':
                            ans += 1

    return ans

def enhance(input):
    output = []
    for x in range(-1,len(input)+1):
        row = ''
        for y in range(-1,len(input[0])+1):
            row += algorithm[numX(input,x,y)]
        output.append(row)

    return output

ans = 0
for i in range(50):
    output1 = enhance(input_image)
    if algorithm[0] == '#':
        flag = not flag
    input_image = output1

for x in range(len(input_image)):
    for y in range(len(input_image[x])):
        if input_image[x][y] == '#':
            ans += 1

print(ans)
