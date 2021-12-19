#!/usr/bin/env python3

import time

rot = []
for i in (1,-1):
    for j in (1,-1):
        for k in (1,-1):
            rot.append((i,j,k))
shuffle = [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]]

flag = False

class Scanner:
    def __init__(self, measures):
        self.data = measures
        self.num_data = list(map(pToNum, measures))
    
    def has12Common(self, scannerb):
        for i in range(len(self.data)):
            for r in rot:
                for s in shuffle:
                    start_time = time.time()
                    man_data = self.center(r,s)
                    man_data_num = list(map(pToNum, man_data))
                    for j in range(len(scannerb.data)):
                        # print("1:--- %s seconds ---" % (time.time() - start_time))
                        shift = (
                            scannerb.data[j][0] - man_data[i][0],
                            scannerb.data[j][1] - man_data[i][1],
                            scannerb.data[j][2] - man_data[i][2]
                        )
                        # print("2:--- %s seconds ---" % (time.time() - start_time))
                        adjusted = []
                        for d in scannerb.num_data:
                            adjusted.append(d-pToNum(shift))
                        # scannerb.adjust(shift[0],shift[1],shift[2])
                        # print("3:--- %s seconds ---" % (time.time() - start_time))
                        common = intersectionLen(man_data_num,adjusted)
                        # print("4:--- %s seconds ---" % (time.time() - start_time))
                        if common >= 12:
                            self.data = man_data
                            self.data = self.adjust(-shift[0],-shift[1],-shift[2])
                            self.num_data = list(map(pToNum, self.data))
                            return (shift,r,s)
                        # quit()

    def adjust(self, x, y, z):
        changed_data = []
        for d in self.data:
            changed_data.append((
                d[0] - x,
                d[1] - y,
                d[2] - z
            ))
        return changed_data

    def center(self,r,s):
        changed_data = []
        for d in self.data:
            changed_data.append((
                d[s[0]] * r[0],
                d[s[1]] * r[1],
                d[s[2]] * r[2]
            ))
        return changed_data

# f = open("puzzle_test.txt","r")
f = open("puzzle.txt","r")
lines = f.readlines()

def pToNum(p):
    return p[0] * 200001 * 200001 + p[1] * 200001 + p[2]

def intersectionLen(listA, listB):
    return len(set(listA) & set(listB))
    # inside = {}
    # for a in listA:
    #     inside[pToNum(a)] = True
    
    # ans = 0
    # for b in listB:
    #     if pToNum(b) in inside:
    #         ans += 1

    # return ans

def union(listA, listB):
    # print(sorted(listA, key=pToNum))
    # print(sorted(listB, key=pToNum))
    inside = {}
    for a in listA:
        inside[pToNum(a)] = True
    
    for b in listB:
        if pToNum(b) in inside:
            continue
        listA.append(b)

    return listA

scanners = []
scanner_data = []
for line in lines:
    if line[0] == '-' and line[1] == '-':
        scanner_data = []
        continue
    if line[0] == '\n':
        scanners.append(Scanner(scanner_data))
        continue
    scanner_data.append(tuple(map(int, line[:-1].split(','))))
scanners.append(Scanner(scanner_data))

# for i in range(len(scanners)):
    # for j in range(len(scanners)):
        # print(i,j,scanners[j].has12Common(scanners[i]))

matched = {0}
def match(scanId):
    for u in range(len(scanners)):
        if u in matched:
            continue
        start_time = time.time()
        val = scanners[u].has12Common(scanners[0])
        # print("1:--- %s seconds ---" % (time.time() - start_time))
        if val is not None:
            print(u," shares common with",scanId,val)
            matched.add(u)
            match(u)
            # scanners[0].data = union(scanners[0].data, scanners[u].data)
            # scanners[0].num_data = list(map(pToNum, scanners[0].data))
            continue

ans = []
for i in range(len(scanners)):
    ans = union(ans,scanners[i].data)
print(len(ans))


