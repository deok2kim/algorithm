def check(answer):
    for x, y, structure in answer:
        if structure == 0:  # 기둥
            # 아래 바닥 or 아래 기둥 or 왼쪽 보 or 오른쪽 보
            if y == 0 or (x, y - 1, 0) in answer or (x - 1, y, 1) in answer or (x, y, 1) in answer:
                continue
            else:
                return False
        else:  # 보
            # 아래 기둥 or 오른쪽 아래 기둥 or (왼쪽 보 and 오른쪽 보)
            if (x, y - 1, 0) in answer or (x + 1, y - 1, 0) in answer or (
                    (x - 1, y, 1) in answer and (x + 1, y, 1) in answer):
                continue
            else:
                return False

    return True


def solution(n, build_frame):
    # set을 쓰는 이유: if a in lst 와 같이 어떤 리스트안에 값이 들어있는지 없는지 확인할 때 set이 훨씬 빠르다
    answer = set()

    for x, y, structure, action in build_frame:
        # set에는 list형태를 add할 수 없다. 나중에 바꿔줘야 해서 귀찮다.. 하지만 속도
        xys = (x, y, structure)
        if action == 1:  # 설치
            answer.add(xys)  # 일단 설치해보고
            if not check(answer):  # 문제가 발생하면
                answer.remove(xys)  # 다시 삭제

        else:  # 삭제
            answer.remove(xys)  # 일단 삭제하고
            if not check(answer):  # 문제가 발생하면
                answer.add(xys)  # 다시 추가

    # 정렬...
    answer = [list(ans) for ans in answer]
    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer


qq = [
    [5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
         [3, 2, 1, 1]], ],
    [5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
         [1, 1, 1, 0], [2, 2, 0, 1]]]
]

for q in qq:
    print(solution(q[0], q[1]))
