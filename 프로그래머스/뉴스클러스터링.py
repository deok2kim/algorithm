from collections import defaultdict


def make_set(s):
    my_set = defaultdict(int)
    for i in range(len(s) - 1):
        word = s[i:i + 2].upper()
        if word.isalpha():
            my_set[word] += 1

    return my_set


def intersect(s1, s2):
    cnt = 0
    for key in s1:
        if s2.get(key):
            cnt += min(s1[key], s2[key])
    return cnt


def union(s1, s2):
    cnt = 0
    for key in s1:
        if s2.get(key):
            cnt += max(s1[key], s2[key])
        else:
            cnt += s1[key]

    for key in s2:
        if not s1.get(key):
            cnt += s2[key]

    return cnt


def solution(str1, str2):
    answer = 0
    str1_set = make_set(str1)
    str2_set = make_set(str2)
    intersecting_count = intersect(str1_set, str2_set)
    union_count = union(str1_set, str2_set)

    answer += int(intersecting_count / union_count * 65536) if union_count else 65536
    return answer


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', '	AAAA12'))
