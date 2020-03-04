def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        tmp_list = []
        for j in range(len(arr2[0])):
            tmp_sum = 0
            for k in range(len(arr1[0])):
                tmp_sum += arr1[i][k]*arr2[k][j]
            tmp_list.append(tmp_sum)
        answer.append(tmp_list)
    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
