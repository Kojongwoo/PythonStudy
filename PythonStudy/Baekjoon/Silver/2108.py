import sys
from collections import defaultdict

input = sys.stdin.readline
sum = 0
mean = 0
median = 0
mode = 0
gap = 0
mid_index = 0
min = 0
max = 0

N = int(input())
list = [0] * N
count = [0] * N

for i in range(0, N):
    a = int(input())
    list[i] = a
    sum += list[i]

list = sorted(list)
min = list[0]
max = list[-1]
mean = round(sum / N)

mid_index = N // 2
median = list[mid_index]

frequency = defaultdict(int)
max_count = 0

for num in list:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
    if frequency[num] > max_count:
        max_count = frequency[num]

modes = []
for num, count in frequency.items():
    if count == max_count:
        modes.append(num)

if len(modes) > 1:
    mode = sorted(modes)[1]
else:
    mode = modes[0]

gap = max - min

print(mean)
print(median)
print(mode)
print(gap)
