#!/usr/bin/env python3

f = open("puzzle.txt","r")
lines = f.readlines()

nums = lines[0][:-1].split(",")
for i in range(len(nums)):
	nums[i] = int(nums[i])
nums = sorted(nums)

def price(k):
	val = 0
	for num in nums:
		val += (abs(k-num) * (abs(k-num)+1)) // 2
	return val

ans = price(nums[-1])
for i in range(nums[0],nums[-1]):
	ans = min(ans, price(i))

print(ans)
