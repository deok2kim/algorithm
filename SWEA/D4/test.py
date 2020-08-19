def solution(clothes):
    clothes_dic = {}
    for i in clothes:
        tmp = i[1]
        if clothes_dic.get(tmp):
            clothes_dic[tmp] += 1
        else:
            clothes_dic[tmp] = 1

    print(clothes_dic)
    for i in clothes_dic.values():
        print(i)
    return
print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]    ))