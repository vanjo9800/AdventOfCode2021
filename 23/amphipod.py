#!/usr/bin/env python3

f = open("puzzle_test.txt","r")
f = open("puzzle.txt","r")
lines = f.readlines()

hallway = '...........'
rooms = ''
for j in [3,5,7,9]:
    for i in [2,3,4,5]:
        rooms += lines[i][j]

visited = {}
depth = {}
queue = [hallway + rooms]
visited[hallway + rooms] = 0
depth[hallway + rooms] = 0

def freePass(h,i,j):
    for k in range(i+1,j+1):
        if h[k] != '.':
            return False
    for k in range(j,i):
        if h[k] != '.':
            return False
    return True

def dist(i,j):
    if i < j:
        return j-i
    else:
        return i-j

place = {
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8
}

roomOffset = {
    'A' : 0,
    'B' : 4,
    'C' : 8,
    'D' : 12
}

mult = {
    'A' : 1,
    'B' : 10,
    'C' : 100,
    'D' : 1000
}

roomEnd = {
    0 : 'A',
    4 : 'B',
    8 : 'C',
    12 : 'D'
}

def byPrice(a):
    return visited[a]
 
loop=0

while len(queue) > 0:
    queue.sort(key=byPrice)
    t = queue[0]
    if t == '...........AAAABBBBCCCCDDDD':
        break
    h = t[0:11]
    r = t[11:]
    price = visited[t]
    print(price)
    queue.pop(0)

    for i in range(len(h)):
        if h[i] != '.' and freePass(h,i,place[h[i]]):
            nH = list(h)
            nR = list(r)
            nPr = price
            for k in range(4):
                if r[roomOffset[h[i]]:k + 1 + roomOffset[h[i]]] == (k+1) * '.' and r[k + 1 + roomOffset[h[i]]: 4 +roomOffset[h[i]]] == (3-k) * h[i]:
                    nR[k + roomOffset[h[i]]] = h[i]
                    nH[i] = '.'
                    nPr += (dist(i,place[h[i]]) + k + 1) * mult[h[i]]
            m = ''.join(nH) + ''.join(nR)
            if m not in visited or visited[m] > nPr:
                visited[m] = nPr
                if m not in queue:
                    queue.append(m)
                    # print("Adding", m, nPr)

    for top in [0,4,8,12]:
        for d in range(4):
            if r[top+d] != '.' and (r[top+d] != roomEnd[top] or r[top+d+1:top+4] != (3-d) * roomEnd[top]):
                for next in [0,1,3,5,7,9,10]:
                    if h[next] == '.' and freePass(h,top//2+2,next):
                        nH = list(h)
                        nR = list(r)
                        nR[top+d] = '.'
                        nH[next] = r[top+d]
                        m = ''.join(nH) + ''.join(nR)
                        nPr = price + (dist(top//2+2,next) + d + 1) * mult[r[top+d]]
                        if m not in visited or visited[m] > nPr:
                            visited[m] = nPr
                            if m not in queue:
                                queue.append(m)
                                # print("Adding", m, nPr)
                break

    # quit()
    loop -= 1
    if loop == 0:
        # quit()
        pass

print("Ans:", visited['...........AAAABBBBCCCCDDDD'])
