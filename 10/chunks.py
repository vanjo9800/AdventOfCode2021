#!/usr/bin/env python3

f = open("puzzle.txt","r")
lines = f.readlines()

res = []
for line in lines:
	log = []
	isCorrupted = False
	for bracket in line:
		if bracket == '(' or bracket == '[' or bracket == '{' or bracket == '<':
			log.append(bracket)
		if bracket == ')':
			if log[-1] == '(':
				log.pop()
			else:
				isCorrupted = True
		if bracket == ']':
			if log[-1] == '[':
				log.pop()
			else:
				isCorrupted = True
		if bracket == '}':
			if log[-1] == '{':
				log.pop()
			else:
				isCorrupted = True
		if bracket == '>':
			if log[-1] == '<':
				log.pop()
			else:
				isCorrupted = True

	if isCorrupted:
		continue

	ans = 0
	for symb in log[::-1]:
		ans *= 5
		if symb == '(':
			ans += 1
		if symb == '[':
			ans += 2
		if symb == '{':
			ans += 3
		if symb == '<':
			ans += 4
	res.append(ans)

res.sort()
print(res[len(res)//2])
