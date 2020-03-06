def solution(w, h):
    answer = 1

    # 두 수의 최대 공약수
    def gdc(a, b):
        x, y = max(a, b), min(a, b)
        while True:
            if x == 1 or y == 1:
                return 1

            if x % y == 0:
                return y

            else:
                x, y = y, x % y

    Repetition = gdc(w, h)
    print('최대공약수', Repetition)
    entire = w * h
    torn = ((w // Repetition) + (h // Repetition) - 1) * Repetition
    answer = entire - torn

    return answer


print(solution(8, 12))
print(solution(7, 14))
print(solution(2, 5))
print(solution(1, 2))
print(solution(3, 3))
print(solution(5, 10))
print(solution(10, 7))