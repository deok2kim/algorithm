import math

N = int(input())
applicant_list = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for applicant in applicant_list:
    answer += 1
    applicant -= B
    if applicant > 0:
        answer += math.ceil(applicant / C)

print(answer)
