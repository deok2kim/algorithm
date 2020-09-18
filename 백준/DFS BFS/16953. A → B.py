def solution(A, B):
    answer = 1

    def cal(num):
        nonlocal answer
        if num > A:

            if num % 10 == 1:
                answer += 1
                cal(num // 10)
            else:
                if num % 2 == 0:
                    answer += 1
                    cal(num // 2)
                else:
                    answer = -1
                    return
        elif num < A:
            answer = -1
            return

    cal(B)
    print(answer)


if __name__ == "__main__":
    A0, B0 = map(int, input().split())
    solution(A0, B0)
