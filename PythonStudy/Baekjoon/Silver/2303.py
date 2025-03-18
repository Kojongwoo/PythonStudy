# from itertools import combinations

N = int(input())
number = []
count = 0
max_score = 0

for _ in range(N):
    cards = list(map(int, input().split()))
    max_units = 0   # 일의 자리 수 최대값을 0으로 초기화

    for i in range(0, 5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                units = (cards[i] + cards[j] + cards[k]) % 10
                if units > max_units:
                    max_units = units
    
    number.append(max_units)

for i in range(N):
    if number[i] >= max_score:
        max_score = number[i]
        count = i + 1
print(count)

# # =================== 조합 ==================
# from itertools import combinations
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# ans = 0
# ans_max = 0
# for i in range(n):
#     combi = list(combinations(arr[i], 3))
#     temp = 0
#     for j in combi:
#         temp = max(temp, sum(j) % 10)
#     if temp >= ans_max:
#         ans = i + 1
#         ans_max = temp
# print(ans)
