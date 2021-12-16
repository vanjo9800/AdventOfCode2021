#!/usr/bin/env python3

f = open("puzzle.txt","r")
lines = f.readlines()

field = []

for line in lines:
	field.append(list(line[:-1]))

def findBasin(i,j):
	points = []
	points.append((i,j))
	
	sz = 0
	while len(points):
		x,y = points[0]
		points.pop(0)
		if field[x][y] == '9':
			continue
		field[x][y] = '9'
		sz += 1
		if x > 0 and field[x-1][y] != '9':
			points.append((x-1,y))
		if x + 1 < len(field) and field[x+1][y] != '9':
			points.append((x+1,y))
		if y > 0 and field[x][y-1] != '9':
			points.append((x,y-1))
		if y + 1 < len(field[x]) and field[x][y+1] != '9':
			points.append((x,y+1))

	return sz

ans=0
basins = []
for i in range(len(field)):
	for j in range(len(field[i])):
		isLow = True
		if i > 0 and field[i-1][j] <= field[i][j]:
			isLow = False
		if i + 1 < len(field) and field[i+1][j] <= field[i][j]:
			isLow = False
		if j > 0 and field[i][j-1] <= field[i][j]:
			isLow = False
		if j + 1 < len(field[i]) and field[i][j+1] <= field[i][j]:
			isLow = False
		if isLow:
			size = findBasin(i,j)
			basins.append(size)

basins.sort(reverse = True)
print(basins[0] * basins[1] * basins[2])
