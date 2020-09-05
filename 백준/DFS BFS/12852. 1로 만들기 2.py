def cal(n, lst):
    global answer_cnt, answer_list
    # print(answer_list)
    # print(n, lst)
    length_lst = len(lst)
    if length_lst > answer_cnt:
        return

    if n == 1:
        if length_lst < answer_cnt:
            answer_cnt = length_lst
            answer_list = lst[:]
            # print(lst)
        # print(answer_cnt, answer_list)
        return

    else:
        if n % 3 == 0:
            cal(n//3, lst + [n//3])

        if n % 2 == 0:
            cal(n // 2, lst + [n//2])

        cal(n-1, lst+[n-1])


N = int(input())
answer_cnt, answer_list = float('inf'), []
cal(N, [N])
# print(answer_list)
print(answer_cnt-1)
print(*answer_list)
