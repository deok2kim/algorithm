def solution(record):

    users = {}
    log = []
    for rec in record:
        r = rec.split()
        userId = r[1]
        if r[0] == 'Enter':
            nickname = r[2]
            users[userId] = nickname
        elif r[0] == 'Change':
            changeNickname = r[2]
            users[userId] = changeNickname

        log.append((userId, r[0]))

    answer = []
    for l in log:
        if l[1] == 'Enter':
            msg = f'{users[l[0]]}님이 들어왔습니다.'
        elif l[1] == 'Leave':
            msg = f'{users[l[0]]}님이 나갔습니다.'
        else:
            continue

        answer.append(msg)
    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
