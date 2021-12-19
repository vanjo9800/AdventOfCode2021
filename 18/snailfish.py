#!/usr/bin/env python3

import re

f = open("puzzle_test.txt","r")
f = open("puzzle.txt","r")
lines = f.readlines()

# def convert(str_snailfish):
#     snailfish = []
#     if str_snailfish[0] == '[':
#         first_part, len1 = convert(str_snailfish[1:])
#         second_part, len2 = convert(str_snailfish[1+len1+1:])
#         str_snailfish = (first_part, second_part)
#         return (str_snailfish, len1+len2+3)
#     return (int(str_snailfish), len(str(int(str_snailfish))))    

def normalise(snailfish):
    temp = re.findall(r'\d+', snailfish)
    nums = list(map(int, temp))
    
    index = 0
    nested = 0
    ans = []
    i = 0

    while i < len(snailfish):
        c = snailfish[i]
        if c.isdigit():
            i += len(str(nums[index]))
            # if nums[index] >= 10:
            #     ans.append('[')
            #     ans.append(nums[index] // 2)
            #     ans.append(',')
            #     if nums[index] % 2 == 1:
            #         ans.append((nums[index] // 2) + 1)
            #     else:
            #         ans.append(nums[index] // 2)
            #     ans.append(']')
            #     ans.append(snailfish[i:])
            #     # print("Condense","".join(map(str,ans)))
            #     return "".join(map(str,ans))
            ans.append(nums[index])
            index += 1
            continue
        if c == ',':
            i += 1
            ans.append(',')
            continue
        if c == '[':
            nested += 1
            ans.append('[')
            i += 1
            continue
        if c == ']':
            i += 1
            nested -= 1
            if nested < 4:
                ans.append(']')
            else:
                # explode
                ans.pop() #num2
                ans.pop() #,
                ans.pop() #num1
                ans.pop() #[
                index -= 1
                newRem = snailfish[i:]
                if index + 1 < len(nums):
                    newRem = newRem.replace(str(nums[index+1]), str(nums[index+1]+nums[index]), 1)
                    del nums[index]
                index -= 1
                if index > 0:
                    for j in range(1,len(ans)+1):
                        if ans[-j] == nums[index-1]:
                            ans[-j] += nums[index]
                            break
                    del nums[index]
                ans.append(newRem)
                ansAll = "".join(map(str,ans))
                ansAll = ansAll.replace('[,','[0,')
                ansAll = ansAll.replace(',]',',0]')
                return ansAll

    snailfish = "".join(map(str,ans))
    temp = re.findall(r'\d+', snailfish)
    nums = list(map(int, temp))
    
    index = 0
    nested = 0
    ans = []
    i = 0

    while i < len(snailfish):
        c = snailfish[i]
        if c.isdigit():
            i += len(str(nums[index]))
            if nums[index] >= 10:
                ans.append('[')
                ans.append(nums[index] // 2)
                ans.append(',')
                if nums[index] % 2 == 1:
                    ans.append((nums[index] // 2) + 1)
                else:
                    ans.append(nums[index] // 2)
                ans.append(']')
                ans.append(snailfish[i:])
                # print("Condense","".join(map(str,ans)))
                return "".join(map(str,ans))
            ans.append(nums[index])
            index += 1
            continue
        if c == ',':
            i += 1
            ans.append(',')
            continue
        if c == '[':
            nested += 1
            ans.append('[')
            i += 1
            continue
        if c == ']':
            i += 1
            nested -= 1
            if nested < 4:
                ans.append(']')
            else:
                # explode
                ans.pop() #num2
                ans.pop() #,
                ans.pop() #num1
                ans.pop() #[
                index -= 1
                newRem = snailfish[i:]
                if index + 1 < len(nums):
                    newRem = newRem.replace(str(nums[index+1]), str(nums[index+1]+nums[index]), 1)
                    del nums[index]
                index -= 1
                if index > 0:
                    for j in range(1,len(ans)+1):
                        if ans[-j] == nums[index-1]:
                            ans[-j] += nums[index]
                            break
                    del nums[index]
                ans.append(newRem)
                ansAll = "".join(map(str,ans))
                ansAll = ansAll.replace('[,','[0,')
                ansAll = ansAll.replace(',]',',0]')
                return ansAll

def reduce(number):
    # print(number)
    newNum = normalise(number)
    while newNum is not None:
        number = newNum
        # print(number)
        newNum = normalise(number)
    # print(number)
    return number

def sum(snailfish):
    temp = re.findall(r'\d+', snailfish)
    nums = list(map(int, temp))
    
    index = 0
    ans = []
    i = 0

    while i < len(snailfish):
        c = snailfish[i]
        if c.isdigit():
            i += len(str(nums[index]))
            ans.append(nums[index])
            index += 1
            continue
        if c == ',':
            i += 1
            ans[-1] *= 3
            continue
        if c == '[':
            i += 1
            continue
        if c == ']':
            i += 1
            ans[-1] *= 2
            ans[-2] += ans[-1]
            ans.pop()
    return ans[0]


last = None
for line in lines:
    if last is None:
        last = line[:-1]
        continue
    last = reduce('[' + last + ',' + line[:-1] + ']')

maxN = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if i == j:
            continue
        maxN = max(maxN, sum(reduce('[' + lines[i][:-1] + ',' + lines[j][:-1] + ']')))

print(last)
print(sum(last))
print(maxN)
