#!/usr/bin/env python3

f = open("puzzle_test.txt","r")
# f = open("puzzle_easy.txt","r")
f = open("puzzle.txt","r")
map = f.readlines()

step = 1

for i in range(len(map)):
    map[i] = list(map[i][:-1])

while True:
    moved = False

    move = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '>':
                next = (j+1) % (len(map[i]))
                if map[i][next] == '.':
                    move.append((i,j,next))
    for (i,j,next) in move:
        map[i][next] = map[i][j]
        map[i][j] = '.'
        moved = True

    move = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'v':
                next = (i+1) % (len(map))
                if map[next][j] == '.':
                    move.append((i,j,next))
    for (i,j,next) in move:
        map[next][j] = map[i][j]
        map[i][j] = '.'
        moved = True

    # for i in range(len(map)):
    #     print(''.join(map[i]))
    # print()
    # quit()

    if not moved:
        break
    step += 1

print(step)
