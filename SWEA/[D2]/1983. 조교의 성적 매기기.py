import math
T = int(input())

for t in range(1, T + 1):
    n, m = map(int, input().split())
    rank = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    scores = []
    for i in range(n):
        score = list(map(int, input().split()))
        scores.append(round(score[0]*0.35 + score[1]*0.45 + score[2]*0.20, 3))

    student_score = scores[m-1]
    scores.sort(reverse=True)
    result = math.ceil((scores.index(student_score) + 1)*10/n)
    print('#{} {}'.format(t, rank[result-1]))
    