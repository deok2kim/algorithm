def add_lesson():
    cnt = 0  # 레코드 갯수 세기
    sum_lesson = 0  # 한 레코드에 들어갈 레슨들의 합
    for i in range(N):
        if sum_lesson + lesson_list[i] > mid:
            cnt += 1
            sum_lesson = 0

        sum_lesson += lesson_list[i]
    else:
        if sum_lesson:
            cnt += 1
    return cnt


if __name__ == "__main__":
    N, M = map(int, input().split())  # N: 레슨 수, M: 블루레이 수
    lesson_list = list(map(int, input().split()))  # 레슨들

    right = sum(lesson_list)   # 레슨을 하나의 레코드에 다 담을 수 있을 때 레코드의 크기는 레슨의 합이다
    left = max(lesson_list)  # 레코드가 가질 수 있는 가장 작은 크기
    while left <= right:
        # 레코드 크기 중간값 구하기
        mid = (left + right) // 2
        cnt = add_lesson()
        if cnt <= M:  # 레코드 숫자가 모자라면 레코드 크기(mid)를 줄인다.
            right = mid - 1
        elif cnt > M:  # 레코드 숫자가 더 많아지면 레코드 크기(mid)를 늘린다
            left = mid + 1

    # 답은 left 에 있다. (최소 크기)
    print(left)

