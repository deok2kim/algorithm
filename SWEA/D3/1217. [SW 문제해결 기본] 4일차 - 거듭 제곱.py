# 재귀 호출 이용하여 거듭제곱 구하기
def power(a, idx=1):
    global answer
    if idx == m:
        answer = a
        return
    else:
        power(a * n, idx + 1)


for tc in range(1, 11):
    input()
    n, m = map(int, input().split())
    answer = 0
    power(n)

    print('#{} {}'.format(tc, answer))
