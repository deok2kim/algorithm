def bt(cnt):
    global result, check

    # 가지치기 | 얻을 수 있는 최댓값을 찾았을 때 모든 재귀함수를 정지 - check
    if max_numbers == numbers:
        # 남은 교환 횟수가 짝 수 일때는 다시원래대로 돌릴 수 있으므로 그냥 뽑아준다.
        # 남은 교환 횟수가 홀 수 일때
        if (n-cnt) % 2:
            # 중복 숫자가 있을 때는 중복 숫자를 서로 바꿔줄 수 있으므로 그냥 뽑아준다.
            # 중복 숫자가 없을 때 | 제일 마지막의 두 숫자의 위치를 바꿔준다
            if len(numbers) == len(set(numbers)):
                numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
        check = True
        result = numbers[:]
        return

    # 함수 정지 조건
    if cnt == n:
        if numbers > result:
            result = numbers[:]
        return

    # 완전 탐색 돌리기
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            # max 값을 찾아서 모든 함수 종료
            if check:
                return
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                bt(cnt + 1)
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return


for tc in range(1, int(input()) + 1):
    numbers, n = input().split()
    numbers = list(map(int, numbers))
    n = int(n)
    result = []
    max_numbers = sorted(numbers, reverse=True)
    check = False
    bt(0)
    print('#{} {}'.format(tc, ''.join(list(map(str, result)))))

'''
3
123 1
2737 1
32888 2
'''