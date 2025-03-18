K = int(input())
stack = []
sum = 0
for _ in range(K):
    a = int(input())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

if not stack:
    print(0)
else:
    for i in range(0, len(stack)):
        sum += stack[i]
    print(sum)
