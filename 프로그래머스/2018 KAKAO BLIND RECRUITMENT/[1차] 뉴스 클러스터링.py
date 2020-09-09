def solution(str1, str2):
    answer = 0
    a_list = [str1[i:i+2].upper()  for i in range(len(str1)-1) if str1[i:i+2].upper().isalpha()]
    b_list = [str2[i:i+2].upper()  for i in range(len(str2)-1) if str2[i:i+2].upper().isalpha()]
    print(a_list)
    print(b_list)
    # 교집합
    kyo = 0
    kyo_list = set()
    for a in a_list:
        if a not in kyo_list:
            tmp1 = min(a_list.count(a), b_list.count(a))
            if tmp1:
                kyo += tmp1
                kyo_list.add(a)

    # 합집합
    hap_list = set()
    hap = 0
    for a in a_list:
        if a not in hap_list:
            tmp2 = max(a_list.count(a), b_list.count(a))
            hap += tmp2
            hap_list.add(a)

    for b in b_list:
        if b not in hap_list:
            tmp2 = max(a_list.count(b), b_list.count(b))
            hap += tmp2
            hap_list.add(b)

    if hap == 0:
        return 65536
    print(kyo, hap)
    answer = (kyo/hap)*65536
    return int(answer)

print(solution("ab", 'aab'))