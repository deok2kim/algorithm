from itertools import chain  # 2차원리스트 1차원리스트로 만들기


def solution(key, lock):
    lenK = len(key)
    lenL = len(lock)
    # 자물쇠 주위를 빈공간으로 확장해주기 | 인덱스에러방지 - 이 문제의 핵심
    lock = fillAround(lock, key)

    for i in range(4):  # 최초한번, 90, 180, 270 확인
        if cutLock(key, lock):  # 일치하면 True반환하고 끝
            return True
        else:  # 아니면 key를 회전시킨다.
            key = lotationKey(key)

    return False


# 자물쇠 자르기
def cutLock(key, lock):
    # 자물쇠의 열쇠 구멍 갯수
    holeCnt = list((chain.from_iterable(lock))).count(0)
    lenK = len(key)
    lenL = len(lock) - (lenK * 2 - 2)
    for i in range(lenK + lenL - 1):
        for j in range(lenK + lenL - 1):
            # 자물쇠를 열쇠 크기만큼 자르기
            partOfLock = [row[j:j + lenK] for row in lock[i:i + lenK]]

            # tip: 자른 자물쇠의 구멍이 전체 구멍을 포함할 때만 체크하면 된다!
            if list(chain.from_iterable(partOfLock)).count(0) == holeCnt:
                if checkKey(key, partOfLock, holeCnt):
                    return True
    return False


# 열쇠가 맞는 지 확인
def checkKey(key, partOfLock, holeCnt):
    lenK = len(key)
    cnt = 0
    for i in range(lenK):
        for j in range(lenK):

            if key[i][j] == 1:  # 열쇠 돌기와
                if partOfLock[i][j] == 0:  # 자물쇠 구멍이 만나면 O
                    cnt += 1
                elif partOfLock[i][j] == 1:  # 자물쇠 돌기가 만나면 X
                    return False
            else:  # 열쇠 구멍과
                if partOfLock[i][j] == 0:  # 열쇠 구멍이 만나면 X
                    return False

    if cnt == holeCnt:
        return True

    return False


# 자물쇠의 주위를 채워주기 확인!!
def fillAround(lock, key):
    lenL = len(lock)
    lenK = len(key)
    # 위아래 채우기
    newLock = [[9] * lenL] * (lenK - 1) + lock + [[9] * lenL] * (lenK - 1)
    # 양옆 채우기
    for i in range(len(newLock)):
        newLock[i] = [9] * (lenK - 1) + newLock[i] + [9] * (lenK - 1)

    return newLock


# 열쇠 회전하기 확인!
def lotationKey(key):
    lenK = len(key)
    newKey = [[0] * lenK for _ in range(lenK)]
    for i in range(lenK):
        for j in range(lenK):
            newKey[i][j] = key[lenK - j - 1][i]

    return newKey


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
