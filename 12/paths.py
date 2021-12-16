#!/usr/bin/env python3

# f = open("puzzle_test.txt","r")
f = open("puzzle.txt","r")
lines = f.readlines()

paths = {}
for line in lines:
	v1, v2 = line[:-1].split("-")
	if v1 not in paths:
		paths[v1] = []
	paths[v1].append(v2)
	if v2 not in paths:
		paths[v2] = []
	paths[v2].append(v1)

numPaths = 0
visited = {}
isTwo = False
path = []
def dfs(v):
	global numPaths
	global visited
	global isTwo
	global path

	if v == "end":
		path.append(v)
		# print(path)
		path.pop()
		numPaths += 1
		return
	if v.islower():
		if v not in visited:
			visited[v] = 0
		if visited[v] > 1:
			return
		if visited[v] == 1:
			if isTwo or v == "start" or v == "end":
				return
			else:
				visited[v] += 1
				isTwo = True
		else:
			visited[v] += 1
	
	path.append(v)
	for neigh in paths[v]:
		dfs(neigh)
	
	path.pop()
	if v.islower():
		if visited[v] == 2:
			isTwo = False
		visited[v] -= 1

dfs("start")

print(numPaths)
