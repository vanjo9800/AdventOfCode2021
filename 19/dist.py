#!/usr/bin/env python3

# f = open("puzzle_test.txt","r")
f = open("scanners.txt","r")
lines = f.readlines()

scanner = []
for line in lines:
    scanner.append(list(map(int,line[:-1].split(','))))

maxD = 0
for i in range(len(scanner)):
    for j in range(len(scanner)):
        maxD = max(maxD, abs(scanner[i][0] - scanner[j][0]) + abs(scanner[i][1]-scanner[j][1]) + abs(scanner[i][2]-scanner[j][2]))

print(maxD)
