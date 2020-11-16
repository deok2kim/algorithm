from itertools import combinations
from collections import defaultdict





def solution(orders, course):
    answer = []

    def isRight(combi):
        cnt = 0
        for order in orders:
            for c in combi:
                if c not in order:
                    break
            else:
                cnt += 1

        else:
            if cnt >= 2:
                dict_menu[cnt].append(''.join(combi))
                set_menu.add((-cnt, ''.join(combi)))
                ddd[len(combi)].append([cnt, ''.join(combi)])

    set_menu = set()

    dict_menu = defaultdict(list)
    ddd = defaultdict(list)

    for order in orders:

        for combi_cnt in course:
            if len(order) >= combi_cnt:
                # print(order, combi_cnt)
                for combi in combinations(order, combi_cnt):
                    combi = list(combi)
                    combi.sort()
                    # print(combi)
                    isRight(combi)
                    # print('dict: ',dict_menu)


    # print(set_menu)
    # print(dict_menu)

    for key, value in dict_menu.items():
        dict_menu[key].sort(key=lambda x: (-len(x), x))

    # print(dict_menu)


    answer_dict = defaultdict(list)

    # for key, value in dict_menu.items():
    #     nn = len(value[0])
    #     for v in set(value):
    #         if len(v) == nn:
    #             answer_dict[key].append(v)
    #             answer.append(v)

    # print(answer_dict)
    # print()
    # print(ddd)
    aa = set()
    for key in ddd.keys():
        ddd[key].sort(key=lambda x: -x[0])
        max_num = ddd[key][0][0]
        for v in ddd[key]:
            if v[0] == max_num:
                aa.add(v[1])

    # print(aa)
    aa = list(aa)
    aa.sort()
    # print(aa)
    answer = aa
    # for key, value in dict_menu.items():
    #     for v1 in value:
    #         cnt = 0
    #         for v2 in value:
    #             # print('=================',v1, v2)
    #             v1_l = list(v1)
    #             for v1_l_v in v1_l:
    #                 # print(v1_l_v, v1)
    #                 if v1_l_v not in v2:
    #                     # print('멈춘다')
    #                     break
    #             else:
    #                 cnt += 1
    #
    #         else:
    #             if cnt == 1:
    #                 # print(v1)
    #                 if len(answer_dict[key]) > 0:
    #                     if len(answer_dict[key][0]) > len(v1):
    #                         pass
    #                 answer_dict[key].append(v1)
    #                 # answer.append(v1)
    # print(answer_dict)
    # for key in answer_dict.keys():
    #     answer_dict[key].sort()
    #
    # for key, value in answer_dict.items():
    #      answer += value
    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]	))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
# print(solution(["ABCDE", "AB", "ABC", "BC", "ABC", "CDE"], [2,3,5]))
# print(solution(["ABC", "AB", "ABC"], [2,3,5]))
# print(solution(["ABCDE", "CDEFG", "ACE"], [2,3,5]))