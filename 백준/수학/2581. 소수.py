N = int(input())
M = int(input())

answer = []
for number in range(N, M + 1):
    if number == 1:
        continue
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            break
    else:
        answer.append(number)

if answer:
    print(sum(answer))
    print(answer[0])
else:
    print(-1)
