#!/usr/bin/env python3

f = open("puzzle_test.txt","r")
f = open("puzzle.txt","r")
lines = f.readlines()

p = [int(lines[0][28:-1]) - 1,int(lines[1][28:-1]) - 1]

# Task 1

# scores = [0,0]

# dice = 0
# throws = 0
# turn = 0

# while scores[0] < 1000 and scores[1] < 1000:
#     move = 0
#     for i in range(3):
#         move += dice + 1
#         dice += 1
#         dice %= 100
#     throws += 3
#     p[turn] += move
#     p[turn] %= 10
#     scores[turn] += p[turn] + 1

#     turn += 1
#     turn %= 2

# print(scores[turn] * throws)

mem = {}

def add(t1,t2):
    return tuple(map(sum,zip(t1,t2)))

def scale(t,s):
    return tuple([i * s for i in t])

def reverse(tuples):
    new_tup = ()
    for k in reversed(tuples):
        new_tup = new_tup + (k,)
    return new_tup

def wins(p1,p2,s1,s2):
    if (p1,p2,s1,s2) in mem:
        return mem[(p1,p2,s1,s2)]
    
    if s1 >= 21:
        return (1,0)
    if s2 >= 21:
        return (0,1)
    ans = (0,0)

    for next in ([3,1],[4,3],[5,6],[6,7],[7,6],[8,3],[9,1]):
        ans = add(ans, reverse(scale(wins(p2, (p1+next[0])%10, s2, s1 + (p1+next[0])%10 + 1), next[1])))

    # print((p1,p2,s1,s2), ans)
    mem[(p1,p2,s1,s2)] = ans
    return ans

print(wins(p[0],p[1],0,0))
