import sys

input = sys.stdin.readline
N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시각이 빠른걸로 정렬 |
# 시작 시간도 정렬해주는 이유는 [2,2], [1,2] 가 있을 경우 2,2의 회의를 해버리면 1,2 회의를 진행할 수 없음
# 그러므로 정렬을 통해 [1,2] 진행 후 [2,2] 가 진행되게 해야 한다.
end_time = 0
answer = 0
for i in range(N):
    if meetings[i][0] >= end_time:
        answer += 1
        end_time = meetings[i][1]

print(answer)
