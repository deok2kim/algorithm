def solution(n):
    ans = 0
    div_num = []
    tmp_n = n
    while tmp_n > 0:
        tmp_n = tmp_n // 2
        div_num.append(tmp_n)

    div_num.reverse()
    div_num.append(n)
    print(div_num)

    for i in range(len(div_num) - 1):
        if div_num[i + 1] == div_num[i] * 2:
            continue
        else:
            ans += 1

    return ans


print(solution(5))  # 2
print(solution(6))  # 2
print(solution(5000))  # 5