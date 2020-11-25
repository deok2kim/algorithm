if __name__ == '__main__':
    N = int(input())
    TOP = list(map(int, input().split()))
    answer = [0] * N

    for i in range(1, N):
        j = i - 1
        while j >= 0:
            if TOP[i] == TOP[j]:  # 이전과 같을 때
                answer[i] = answer[j]
                break
            elif TOP[i] > TOP[j]:  # 이전보다 높을 때
                j = answer[j] - 1
            else:  # 이전보다 낮을 때
                answer[i] = j + 1
                break

    print(' '.join(list(map(str, answer))))
