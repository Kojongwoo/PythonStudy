import sys
N = int(sys.stdin.readline().strip())
num1 = list(map(int, sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline().strip())
num2 = list(map(int, sys.stdin.readline().strip().split()))

num1 = set(num1)

for j in range(0, M):
    if num2[j] in num1:
        print(1)
    else:
        print(0)
