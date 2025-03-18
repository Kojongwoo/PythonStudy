from collections import deque
import sys
input = sys.stdin.readline()
yp = deque()
result = []
N, K = map(int, input.split())

for i in range(1, N+1):
    yp.append(i)
count = 0

while len(yp) > 0:
    yp.rotate(-(K-1)) # K=3에서 왼쪽으로 2개 이동해야 세번째 요소를 popleft 가능
    yp.popleft()
    if len(yp) == 1:
        print(yp.popleft())

# print("<" + ", ".join(map(str, result)) + ">")
# yp.append(yp.popleft())
#     count += 1
# if count == K-1:
    #     result.append(yp.popleft())
    #     count = 0
