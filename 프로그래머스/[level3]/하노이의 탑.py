def solution(n):
    answer = []

    def hanoi(N, start, end, sub):
        if N == 1:
            answer.append([start, end])
            return

        else:
            hanoi(N - 1, start, sub, end)
            answer.append([start, end])
            hanoi(N - 1, sub, end, start)

    hanoi(n, 1, 3, 2)
    return answer


print(solution(4))
print(solution(2))
# def hanoi(n, from_pos, to_pos, sub_pos):
#     print('--------------',n, from_pos, to_pos, sub_pos)
#     if n == 1:
#         print('n==1',from_pos, "->", to_pos)
#         return
#     # 짝수이면 서브랑 투랑 바뀐다!
#     hanoi(n - 1, from_pos, sub_pos, to_pos)
#     print('n==n-1', from_pos, "->", to_pos)
#     hanoi(n - 1, sub_pos, to_pos, from_pos)
# print("n = 1")
# hanoi(1, 1, 3, 2)
# print("n = 2")
# hanoi(2, 1, 3, 2)
# print("n = 3")
# hanoi(3, 1, 3, 2)
# print("n = 4")
# hanoi(4, 1, 3, 2)
