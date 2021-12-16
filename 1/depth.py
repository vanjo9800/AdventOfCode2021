#!/usr/bin/env python3

f = open("puzzle.txt","r")
lines = f.readlines()

last = []
ans = 0
for line in lines:
	depth = int(line)
	if len(last) != 3:
		last.append(depth)
		continue
	if last[0] < depth:
		ans = ans + 1
	last.pop(0)
	last.append(depth)

print("Ans: ", ans)
