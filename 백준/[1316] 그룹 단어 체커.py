n = int(input())

cnt = 0  # 조건에 맞는 문자의 갯수
# n만큼 for문을 돌려준다.
for _ in range(n):
    word = input()
    check = set()  # word 의 문자 하나하나를 넣어줄 list
    for i in range(len(word)):
        if i == 0:  # 첫번째 문자는 바로 list 에 넣어주고
            check.add(word[i])
        else:  # 다음 문자부터 체크해준다.
            if word[i] not in check:  # check 에 없으면 문자를 add 해주고
                check.add(word[i])
            else:  # check 에 있을 때
                if word[i] != word[i-1]:  # 바로 이전에 나온 문자가 아니라면 조건에 맞지 않으므로 break
                    break

    else:  # break 없이 모든 문자가 통과하면 조건에 맞는 문자이므로 cnt + 1
        cnt += 1

print(cnt)
