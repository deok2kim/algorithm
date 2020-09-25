

def solution(n):
    answer = 0

    def check(left=1, right=0):
        nonlocal answer
        if left == n and right == n:
            answer += 1
            return

        if left > n or right > n:
            return
        if right > left:
            return

        if left > right:
            check(left+1, right)
            check(left, right+1)

        elif left == right:
            check(left+1, right)

    check()
    return answer

for i in range(1, 15):

    print(solution(i))