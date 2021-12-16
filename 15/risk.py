#!/usr/bin/env python3

# f = open("puzzle_test.txt","r")
f = open("puzzle.txt","r")
lines = f.readlines()

size = len(lines[0])-1

def getVal(i,j):
	val = int(lines[i % size][j % size]) + i//size + j//size
	if val < 10:
		return val
	return val % 10 + 1

minQ = [] 
minQ.append((0,0))

dp = []
visited = []
for i in range(5*size):
	dp.append([size*size*250] * (5*size))
	visited.append([False] * (5*size))
dp[0][0] = 0

def dpComp(a):
	global dp
	return dp[a[0]][a[1]]

while len(minQ) > 0:
	minQ.sort(key=dpComp)
	bestX, bestY = minQ[0]
	minQ.pop(0)
	visited[bestX][bestY] = True

	for (di,dj) in ((-1,0),(1,0),(0,1),(0,-1)):
		if bestX + di >= 0 and bestX + di < 5*size:
			if bestY + dj >= 0 and bestY + dj < 5*size:
				if visited[bestX+di][bestY+dj] == False:
					dp[bestX+di][bestY+dj] = min(dp[bestX+di][bestY+dj], dp[bestX][bestY] + getVal(bestX+di, bestY+dj))
					if (bestX+di, bestY+dj) not in minQ:
						minQ.append((bestX+di, bestY+dj))

print(dp[5*size-1][5*size-1])
