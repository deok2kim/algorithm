def solution(str1, str2):
    def J(ziphap1, ziphap2):
        if ziphap1 == [] and ziphap2 == []:
            return 1

        kyo = set(ziphap1) & set(ziphap2)
        len_kyo = len(kyo)
        for i in kyo:
            x = ziphap1.count(i)
            y = ziphap2.count(i)
            len_kyo += min(x, y) - 1

        hap = set(ziphap1) | set(ziphap2)
        len_hap = len(hap)
        for i in hap:
            x = ziphap1.count(i)
            y = ziphap2.count(i)
            len_hap += max(x, y) - 1
        # print('list', kyo, hap)
        # print(len_kyo, len_hap)

        return len_kyo / len_hap
    # print(str1, str2)
    str1_list = [str1[x:x + 2].lower() for x in range(len(str1) - 1) if str1[x:x + 2].isalpha() and ' ' not in str1[x:x + 2]]
    str2_list = [str2[x:x + 2].lower() for x in range(len(str2) - 1) if str2[x:x + 2].isalpha() and ' ' not in str2[x:x + 2]]
    # print(str1_list, str2_list)
    answer = int(J(str1_list, str2_list) * 65536)
    return answer


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
