def solution(user_id, banned_id):
    len_banned_id = len(banned_id)

    def combi(idx=0):
        if idx == len_banned_id:
            if len(set(answer_tmp)) == len_banned_id:
                # print(answer_tmp)
                answer_tmp.sort()
                answer.add(' '.join(answer_tmp))
            return
        
        if len(set(answer_tmp)) != idx:
            return

        for i in range(len(result[idx])):
            # print(idx, i)
            answer_tmp.append(result[idx][i])
            combi(idx+1)
            answer_tmp.remove(result[idx][i])
            
        return

    answer = set()
    answer_tmp = []
    result = []
    for ban in banned_id:
        tmp = []
        for user in user_id:
            if len(ban) == len(user):
                for i in range(len(ban)):
                    if ban[i] == '*' or ban[i] == user[i]:
                        pass
                    else:
                        break
                else:
                    tmp.append(user)
        result.append(tmp)

    # print(result)
    combi()
    # print(answer)
    answer = len(answer)
    return answer





print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]	))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))