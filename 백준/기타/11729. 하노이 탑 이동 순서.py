def hanoi(n, start, end, sub):
    if n == 1:
        # print(f'{start}=>{end}')
        answer.append([start, end])
        return

    hanoi(n - 1, start, sub, end)
    # print(f'{start}=>{end}')
    answer.append([start, end])
    hanoi(n - 1, sub, end, start)


N = int(input())
answer = []
hanoi(N, 1, 3, 2)
# 출력
print(len(answer))
for i in answer:
    print(*i)
