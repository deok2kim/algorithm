from collections import Counter


def solution(a):
    # 주어진 배열의 숫자의 개수를 구한다.
    number_cnt = Counter(a)
    answer = 0

    # 구한 숫자를 하나 씩 꺼내서
    for standard_number in number_cnt.keys():
        if number_cnt[standard_number] * 2 < answer:  # 이전에 완성한 스타수열의 길이보다 꺼낸 숫자의 개수가 적으면
            continue                                    # 스타수열을 완성해도 길이가 짧으므로 패스

        number_index_list = []  # 주어진 배열에서 꺼낸 숫자의 인덱스를 구한다.
        for i in range(len(a)):
            if a[i] == standard_number:
                number_index_list.append(i)

        seq = []  # 스타수열을 저장할 배열
        before_selected_idx = -1  # 꺼낸 숫자의 왼쪽 or 오른쪽의 숫자를 사용할 때 겹쳐서 사용하지 않기 위해서
        cnt = 0  # 스타수열의 길이 저장
        for idx in number_index_list:
            if 0 <= idx - 1 != before_selected_idx and a[idx] != a[idx - 1]: # 기준 숫자의 왼쪽 숫자 사용
                seq.append([a[idx - 1], a[idx]])
                before_selected_idx = idx - 1
                cnt += 1
            elif len(a) > idx + 1 != before_selected_idx and a[idx] != a[idx + 1]: # 기준 숫자의 오른쪽 숫자 사용
                seq.append([a[idx], a[idx + 1]])
                before_selected_idx = idx + 1
                cnt += 1

        else:
            answer = cnt * 2

    return answer


print(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))
