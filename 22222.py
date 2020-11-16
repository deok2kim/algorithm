def solutioin(S):
    answer = []
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            print(i, j)
            if i != j:
                print(S[i], S[j])
                for k in range(len(S[i])):
                    if S[i][k] == S[j][k]:
                        answer = [i, j, k]
                        print(answer)

    return answer
print(solutioin(["abc", "bca", "dbe"]))

