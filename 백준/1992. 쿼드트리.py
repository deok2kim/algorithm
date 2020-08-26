from itertools import chain
# 2중 리스트를 단일 리스트로 바꾸기 위해서 chain 함수 사용했음


def compression(lst):
    global answer
    length = len(lst) // 2

    answer += '('

    # 왼쪽 위
    llst = lst[:length]
    for i in range(length):
        llst[i] = llst[i][:length]
    sum_llst = sum(list(map(int, chain.from_iterable(llst))))
    if sum_llst == length ** 2:
        answer += '1'
    elif sum_llst == 0:
        answer += '0'
    else:
        compression(llst)

    # 오른쪽 위
    llst = lst[:length]
    for i in range(length):
        llst[i] = llst[i][length:]
    sum_llst = sum(list(map(int, chain.from_iterable(llst))))
    if sum_llst == length ** 2:
        answer += '1'
    elif sum_llst == 0:
        answer += '0'
    else:
        compression(llst)
    # 왼쪽 아래
    llst = lst[length:]
    for i in range(length):
        llst[i] = llst[i][:length]
    sum_llst = sum(list(map(int, chain.from_iterable(llst))))
    if sum_llst == length ** 2:
        answer += '1'
    elif sum_llst == 0:
        answer += '0'
    else:
        compression(llst)

    # 오른쪽 아래
    llst = lst[length:]
    for i in range(length):
        llst[i] = llst[i][length:]
    sum_llst = sum(list(map(int, chain.from_iterable(llst))))
    if sum_llst == length ** 2:
        answer += '1'
    elif sum_llst == 0:
        answer += '0'
    else:
        compression(llst)

    answer += ')'


# 시작 ----------------------------------------------------
N = int(input())
image = [list(input()) for _ in range(N)]

answer = ''
# 최초 확인
sum_image = sum(list(map(int, chain.from_iterable(image))))
if sum_image == len(image) ** 2:
    answer += '1'
elif sum_image == 0:
    answer += '0'
else:
    compression(image)
print(answer)
