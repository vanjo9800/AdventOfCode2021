#!/usr/bin/env python3

f = open("puzzle.txt","r")
lines = f.readlines()

floor = []
for i in range(1000):
	floor_row = []
	for j in range(1000):
		floor_row.append(0)
	floor.append(floor_row)

for line in lines:
	points = line.split(" -> ")
	point1 = points[0].split(",")
	point1[0] = int(point1[0])
	point1[1] = int(point1[1])
	point2 = points[1][:-1].split(",")
	point2[0] = int(point2[0])
	point2[1] = int(point2[1])

	if point1[0] == point2[0]:
		for i in range (point1[1], point2[1]+1):
			floor[point1[0]][i] += 1
		for i in range (point2[1], point1[1]+1):
			floor[point1[0]][i] += 1
	elif point1[1] == point2[1]:
		for i in range (point1[0], point2[0]+1):
			floor[i][point1[1]] += 1
		for i in range (point2[0], point1[0]+1):
			floor[i][point1[1]] += 1
	else:
		startX = point1[0]
		startY = point1[1]
		moveX = 0
		moveY = 0

		if point1[0] < point2[0]:
			moveX = 1
		else:
			moveX = -1

		if point1[1] < point2[1]:
			moveY = 1
		else:
			moveY = -1

		while startX != point2[0] and startY != point2[1]:
			floor[startX][startY] += 1
			startX += moveX
			startY += moveY
		floor[startX][startY] += 1
cnt = 0
for i in range(1000):
	for j in range(1000):
		if floor[i][j] >= 2:
			cnt += 1

print(cnt)
