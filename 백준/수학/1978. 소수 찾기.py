N = int(input())
numbers = list(map(int, input().split()))
answer = 0
for number in numbers:
    if number == 1:
        continue
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            break
    else:
        answer += 1

print(answer)
