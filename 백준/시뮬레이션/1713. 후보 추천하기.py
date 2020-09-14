if __name__ == "__main__":
    N = int(input())
    M = int(input())
    students = list(map(int, input().split()))

    candidates = []
    # 투표수, 들어온 순서, 학생번호
    candidates.append([1, 0, students[0]])
    # print(candidates)
    for i in range(1, M):
        # print(candidates)
        s = students[i]
        # 학생이 이미 후보에 있을 때
        for j in range(len(candidates)):
            if candidates[j][2] == s:
                candidates[j][0] += 1
                break

        # 학생이 없을 때
        else:
            # 후보가 가득일 때:
            if len(candidates) == N:
                candidates.sort(key=lambda x: (x[0], x[1]))
                candidates.pop(0)

            candidates.append([1, i, students[i]])

    answer = []
    # print(candidates)
    for can in candidates:
        answer.append(can[2])

    answer.sort()
    print(*answer)


