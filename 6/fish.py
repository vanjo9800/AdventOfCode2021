#!/usr/bin/env python3

f = open("puzzle.txt","r")
lines = f.readlines()

# lines[0] = "3,4,3,1,2\n"
# 1 ->
# 2 -> 
# 3 ->
# 4 ->
# 5 ->

cnt = [0,0,0,0,0,0,0,0,0]
fish = lines[0][:-1].split(',')
for num in range(len(fish)):
	fish[num] = int(fish[num])
	cnt[fish[num]] += 1

for day in range(256):
	add = cnt[0]
	cnt.pop(0)
	cnt[6] += add
	cnt.append(add)

ans = 0
for i in range(len(cnt)):
	ans += cnt[i]

print(ans)
