#!/usr/bin/env python3

f = open("puzzle.txt","r")
lines = f.readlines()

hor = 0
ver = 0
aim = 0
for line in lines:
	commands = line.split(" ")
	if commands[0] == "forward":
		hor += int(commands[1])
		ver += int(commands[1]) * aim
	elif commands[0] == "up":
		aim -= int(commands[1])
	elif commands[0] == "down":
		aim += int(commands[1])
	else:
		pass

print("Ans: ", hor*ver)
