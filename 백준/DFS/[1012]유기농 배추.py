def solution(begin, target, words):
    if target not in words:
        answer = 0
    else:
        if begin in words:
            words.remove(begin)
        result = {begin:0}
        stack = [begin]
        visit = [0] * len(words)
        while stack:
            begin = stack.pop(0)
            for word in words:
                cnt = 0
                for k in range(len(word)):
                    if word[k] != begin[k]:
                        cnt += 1
                    if cnt == 2:
                        break
                else:
                    idx = words.index(word)
                    if visit[idx] == 0:
                        visit[idx] = 1
                        stack.append(word)
                        result[word] = result[begin] + 1
        answer = result.get(target)
    print(result)
    return answer

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(solution('hit', 'hot', ['hit','hot','ait']))

