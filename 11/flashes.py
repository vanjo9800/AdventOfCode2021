#!/usr/bin/env python3

f = open("puzzle_test.txt","r")
lines = f.readlines()

field = []
for line in lines:
	numline = []
	for num in line[:-1]:
		numline.append(int(num))
	field.append(numline)

for i in range(1000):
	isFlashed = []
	flashed = []
	for row in range(10):
		isFlashed.append([0] * 10)
		for col in range(10):
			field[row][col] += 1
			if field[row][col] >= 10:
				flashed.append((row,col))

	flashes = 0
	while len(flashed) > 0:
		x,y = flashed[0]
		flashed.pop(0)
		if isFlashed[x][y]:
			continue
		isFlashed[x][y] = 1
		flashes += 1

		for dX in (-1,0,1):
			for dY in (-1,0,1):
				if x+dX >= 0 and x+dX < 10:
					if y+dY >= 0 and y+dY < 10:
						field[x+dX][y+dY] += 1
						if field[x+dX][y+dY] >= 10:
							flashed.append((x+dX,y+dY))
	
	for row in range(10):
		for col in range(10):
			if isFlashed[row][col]:
				field[row][col] = 0

	if flashes == 100:
		print(i)
		quit()

print("Longer...")
