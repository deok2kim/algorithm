# 인풋값 전부 받기
T = int(input())
numbers = [input() for _ in range(T)]

# 계산하기
results = []
for tc in range(T):
    number = numbers[tc]
    answer = 0
    while True:
        sum_num = 0
        for n in number:
            sum_num += int(n)
        
        if sum_num > 9:  # 결과값이 두자리 수 이면 다시 분해해서 더하기
            number = str(sum_num)
        else:
            answer = sum_num
            break
    results.append(answer)

# 결과 출력하기
for tc in range(T):
    print(f'#{tc+1} {results[tc]}')
