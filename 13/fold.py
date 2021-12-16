#!/usr/bin/env python3

# f = open("puzzle_test.txt","r")
f = open("puzzle.txt","r")
lines = f.readlines()

maxX = 1500
maxY = 1500

field = []
for i in range(maxX):
	field.append(['.'] * maxY)

def count():
	global field
	global maxX
	global maxY

	ans = 0
	for i in range(maxX):
		for j in range(maxY):
			if field[i][j] == '#':
				ans += 1
	return ans

def vertical_fold(x):
	global field
	global maxX
	global maxY

	maxY = x
	for i in range(maxX):
		for j in range(x):
			if field[i][j] == '#' or field[i][2*x-j] == '#':
				field[i][j] = '#'

def horizontal_fold(y):
	global field
	global maxX
	global maxY

	maxX = y
	for i in range(y):
		for j in range(maxY):
			if field[i][j] == '#' or field[2*y-i][j] == '#':
				field[i][j] = '#'

stage = 1
for line in lines:
	if line == "\n":
		stage = 2
		continue
	if stage == 1:
		x,y = line[:-1].split(',')
		field[int(y)][int(x)] = '#'
	else:
		sign, val = line[11:-1].split('=')
		if sign == 'x':
			vertical_fold(int(val))
		else:
			horizontal_fold(int(val))
		#for i in range(maxX):
			#print(''.join(field[i]))
		#print(count())
		#quit()


for i in range(maxX):
	print(''.join(field[i][:maxY]))
