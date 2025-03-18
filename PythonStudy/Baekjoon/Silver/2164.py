from collections import deque

N = int(input()) # 카드의 개수

# 순서: 맨 위 카드 버리기 -> 맨 위 카드를 가장 아래 카드 밑으로 옮기기
# N = 4인 경우 1번(Front) -> 2번 -> 3번 -> 4번(Rear)
# N부터 1까지 순으로 큐에 삽입

queue = deque()
# 1부터 N까지 숫자 삽입
#rear = queue[-1]
#front = queue[0]

for i in range(1, N + 1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft() # -> front, 1부터 popleft
    queue.append(queue.popleft()) # popleft 값을  rear, 4에 append

print(queue[0])
