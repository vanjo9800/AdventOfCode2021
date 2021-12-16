#!/usr/bin/env python3

f = open("puzzle.txt","r")
lines = f.readlines()

def contains(str1,str2):
	for symb in str1:
		if symb in str2:
			continue
		return False
	return True

ans = 0
for line in lines:
	mapping = line.split("|")[0][:-1].split(" ")
	mapping = sorted(mapping, key=len)
	num = [""] * 10
	num[1] = mapping[0]
	num[7] = mapping[1]
	num[4] = mapping[2]
	num[8] = mapping[-1]

	oneFour = num[4]
	oneFour = oneFour.replace(num[1][0],'')
	oneFour = oneFour.replace(num[1][1],'')
	for i in range(3,9):
		if len(mapping[i]) == 5:
			# 2,3,5
			if contains(oneFour,mapping[i]):
				num[5] = mapping[i]
			elif contains(num[1],mapping[i]):
				num[3] = mapping[i]
			else:
				num[2] = mapping[i]
		else:
			# 0,6,9
			if contains(num[4],mapping[i]):
				num[9] = mapping[i]
			elif contains(oneFour,mapping[i]):
				num[6] = mapping[i]
			else:
				num[0] = mapping[i]

	output = line.split("|")[1][1:-1].split(" ")
	out = ""
	for word in output:
		for i in range(0,10):
			if contains(word,num[i]) and contains(num[i],word):
				out += str(i)
	ans += int(out)

print(ans)
