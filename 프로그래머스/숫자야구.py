from itertools import permutations


def check(n, c, s, b):
    tmp_s = 0
    for i in range(3):
        if n[i] == c[i]:
            tmp_s += 1
    if tmp_s != s:
        return False

    tmp_b = len((set(n) & set(c))) - s

    if tmp_b != b:
        return False


def solution(baseball):
    answer = 0
    candidates = list(permutations(range(1, 10), 3))
    # print(candidates)

    for num, strike, ball in baseball:
        for candi in candidates[:]:  # 모든 후보군을 파악
            if check([int(i) for i in list(str(num))], candi, strike, ball) is False:
                candidates.remove(candi)

    return len(candidates)


print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))
