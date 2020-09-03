import sys # 10만줄이나 되는 인풋을 빨리 받기 위해 사용함

if __name__ == "__main__":
    for tc in range(1, int(input()) + 1):
        N = int(input())
        scores = []
        for i in range(N):
            scores.append(list(map(int, sys.stdin.readline().split())))

        # 서류점수순위 순으로 정렬해주고
        scores.sort(key=lambda x: x[0])
        # 가장높은 면접점수순위를 저장한다
        highScore2 = float('inf')
        cnt = 0
        for i in range(N):
            # i지원자의 서류점수순위는 어짜피 앞에 나온 지원자들보다 낮다
            # 하지만 면접점수순위가 높으면 합격가능!!
            if scores[i][1] < highScore2:
                highScore2 = scores[i][1]
                cnt += 1
        print(cnt)
