from collections import defaultdict
from collections import deque


def insert(part_trie, rest):
    copy_trie = part_trie
    q = deque(rest)
    while q:
        c = q.popleft()
        if c not in copy_trie:
            copy_trie[c] = [0, {}]
        copy_trie[c][0] += 1
        copy_trie = copy_trie[c][1]


def solution(info, query):
    answer = []

    trie = defaultdict(dict)

    for i in info:
        print(i.split())
        a = i.split()
        insert(trie[a[0]], a[1:])

    print(trie)

    for q in query:
        # print(q)
        q = q.replace(' ', '')
        # print(q)
        qq = q.split('and')
        # print(qq)
        tmp = ''
        tmp2 = ''
        for i in range(len(qq[-1])):
            # print(i, qq[-1])
            if qq[-1][i].isdigit():
                tmp2 = qq[-1][i:]
                qq.append(tmp2)
                tmp = qq[-2][:i]
                qq[3] = tmp
                break
        print('qq', qq)

        # for i in range(len(qq)):
        #     if i == 0:
        #         if qq[i] == '-':
        #             pass
        #     elif i == 1:
        #         pass
        #     elif i == 2:
        #         pass
        #     elif i == 3:
        #         pass
        #     elif i == 4:
        #         pass
        cnt = 0
        for i in info:
            print('--------')
            i = i.split()
            print(i)
            print(qq)
            for j in range(4):
                print('@@@@@',qq[j], i[j])
                if qq[j] == '-' or i[j] == qq[j]:
                    continue
                else:
                    break
            else:
                if int(i[-1]) >= int(qq[-1]):
                    cnt += 1

        else:
            print(cnt)
            answer.append(cnt)

    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
