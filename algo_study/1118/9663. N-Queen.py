def bt(i=0):
    global answer
    if i == N:
        answer += 1
        return

    for j in range(N):
        if row[j] or left[i + j] or right[N - 1 + i - j]:
            continue

        row[j] = left[i + j] = right[N - 1 + i - j] = 1
        bt(i + 1)
        row[j] = left[i + j] = right[N - 1 + i - j] = 0


if __name__ == '__main__':
    N = int(input())
    row, left, right = [0] * N, [0] * (2 * N - 1), [0] * (2 * N - 1)
    answer = 0
    bt()
    print(answer)