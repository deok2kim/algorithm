def solution(new_id):
    answer = ''

    # 1단계
    new_id = new_id.lower()
    print(new_id)

    # 2단계
    tmp = ''
    for w in new_id:
        if w.isalpha():
            tmp += w
        elif w.isdigit():
            tmp += w
        elif w == '-':
            tmp += w
        elif w == '_':
            tmp += w
        elif w == '.':
            tmp += w
    new_id = tmp
    print(new_id)

    # 3단계
    tmp=" "
    for w in new_id:
        if w == '.' and tmp[-1] == '.':
            pass
        else:
            tmp += w
    new_id = tmp[1:]
    print(new_id)

    # 4단계
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    print(new_id)

    # 5단계
    if new_id == '':
        new_id = 'a'
    print(new_id)

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]

    if new_id[-1] == '.':
        new_id = new_id[:-1]

    print(new_id)

    # 7단계
    if len(new_id) <= 2:
        for i in range(3-len(new_id)):
            new_id += new_id[-1]

    print(new_id)

    answer = new_id
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution(	"=.="))