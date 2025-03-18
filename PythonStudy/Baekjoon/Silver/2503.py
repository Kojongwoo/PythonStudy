from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())

num = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

case = permutations(num, 3) 

for _ in range(N):
    answer, strike, ball = map(int, input().split())
    tmp = []

    for check in case:
        count_s = 0
        count_b = 0

        for i, str_answer in enumerate(str(answer)):
            if int(str_answer) == check[i]:
                count_s += 1
            if int(str_answer) != check[i] and int(str_answer) in check:
                count_b += 1

        if count_s == strike and count_b == ball:
            tmp.append(check)
    case = tmp

print(len(case))