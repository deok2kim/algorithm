def solution(begin, target, words):
    global answer
    answer = 50

    def dfs(word):
        # print(word)
        global answer
        if word == target:
            if answer > visit.count(True):
                answer = visit.count(True)
            return

        for i in range(len(words)):
            cnt = 0
            if visit[i] == False:
                for j, k in zip(word, words[i]):
                    if j != k:
                        cnt += 1

                    if cnt > 1:
                        break
                else:
                    visit[i] = True
                    dfs(words[i])
                    visit[i] = False

    if target not in words:
        answer = 0
        return answer

    visit = [False] * len(words)
    dfs(begin)

    return answer


print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
