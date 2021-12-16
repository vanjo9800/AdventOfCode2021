#!/usr/bin/env python3

# f = open("puzzle_test.txt","r")
f = open("puzzle.txt","r")
lines = f.readlines()

polymer = lines[0][:-1]
pairs = {}
for i in range(len(polymer)-1):
	pair = polymer[i] + polymer[i+1]
	if pair not in pairs:
		pairs[pair] = 0
	pairs[pair] += 1

table = {}
for i in range(2,len(lines)):
	fr, to = lines[i][:-1].split(" -> ")
	table[fr] = to

for i in range(40):
	new_pairs = {}
	for pair in pairs.keys():
		new_pair_1 = pair[0] + table[pair]
		new_pair_2 = table[pair] + pair[1]
		if new_pair_1 not in new_pairs:
			new_pairs[new_pair_1] = 0
		if new_pair_2 not in new_pairs:
			new_pairs[new_pair_2] = 0
		new_pairs[new_pair_1] += pairs[pair]
		new_pairs[new_pair_2] += pairs[pair]
	pairs = new_pairs

cnt = {}
for pair in pairs.keys():
	if pair[0] not in cnt:
		cnt[pair[0]] = 0
	cnt[pair[0]] += pairs[pair]
cnt[polymer[-1]] += 1

maxn = 0
minx = cnt[list(cnt.keys())[0]]
for c in cnt.keys():
	maxn = max(maxn, cnt[c])
	minx = min(minx, cnt[c])

print(maxn - minx)
