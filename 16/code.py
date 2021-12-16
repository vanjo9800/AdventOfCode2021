# /usr/bin/env python3

f = open("puzzle.txt",'r')

sum = 0
num = f.readline()
#num = 'D2FE28'
num_b = ''

for d in num:
    num_b += str(format(int(d, 16), '0>4b'))

print(num_b)

sum = 0
i = 0
def process(num):
    global sum
    global i

    i += 3
    val = -1
    id = int(num[i:i+3], 2)
    print(id)
    if id == 4:
        i += 3
        val = 0
        while num[i] == '1':
            val *= 16
            val += int(num[i+1:i+5], 2)
            i += 5
        val *= 16
        val += int(num[i+1:i+5], 2)
        i += 5
    else:
        i += 3
        if num[i] == '0':
            length = int(num[i+1:i+16], 2)
            i += 16
            end = i + length
            while i < end:
                if val == -1:
                    val = process(num)
                    continue
                if id == 0:
                    val += process(num)
                elif id == 1:
                    val *= process(num)
                elif id == 2:
                    val = min(val, process(num))
                elif id == 3:
                    val = max(val, process(num))
                elif id == 5:
                    if val > process(num):
                        val = 1
                    else:
                        val = 0
                elif id == 6:
                    if val < process(num):
                        val = 1
                    else:
                        val = 0
                elif id == 7:
                    if val == process(num):
                        val = 1
                    else:
                        val = 0
        else:
            count = int(num[i+1:i+12], 2)
            i += 12
            for j in range(count):
                if val == -1:
                    val = process(num)
                    continue
                if id == 0:
                    val += process(num)
                elif id == 1:
                    val *= process(num)
                elif id == 2:
                    val = min(val, process(num))
                elif id == 3:
                    val = max(val, process(num))
                elif id == 5:
                    if val > process(num):
                        val = 1
                    else:
                        val = 0
                elif id == 6:
                    if val < process(num):
                        val = 1
                    else:
                        val = 0
                elif id == 7:
                    if val == process(num):
                        val = 1
                    else:
                        val = 0
    return val

print(process(num_b))