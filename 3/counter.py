#!/usr/bin/env python3

f = open("puzzle.txt","r")
lines = f.readlines()

#gamma = ""
#epsilon = ""
#for i in range(len(cnt)):
#	if cnt[i] > len(lines)/2:
#		gamma += '1'
#		epsilon += '0'
#	else:
#		gamma += '0'
#		epsilon += '1'

oxygen = lines
co2 = lines

index = 0
while len(oxygen) > 1:
	cnt = 0
	for line in oxygen:
		cnt += int(line[index])
	mc = ''
	if cnt >= len(oxygen)/2:
		mc = '1'
	else:
		mc = '0'
	new_oxygen = []
	for j in range(len(oxygen)):
		if oxygen[j][index] == mc:
			new_oxygen.append(oxygen[j])
	oxygen = new_oxygen
	index += 1

index = 0
while len(co2) > 1:
	cnt = 0
	for line in co2:
		cnt += int(line[index])
	lc = ''
	if cnt >= len(co2)/2:
		lc = '0'
	else:
		lc = '1'
	new_co2 = []
	for j in range(len(co2)):
		if co2[j][index] == lc:
			new_co2.append(co2[j])
	co2 = new_co2
	index += 1

print("Ans: ", int(oxygen[0], 2) * int(co2[0],2))
