def solution(N, dice):
    if N == 1:
        print(sum(dice) - max(dice))
        return
    A, B, C, D, E, F = dice
    # 3 면 4
    face3 = min(list(map(sum, [[A, D, E], [A, E, C], [A, C, B], [A, B, D], [F, B, D], [F, B, C], [F, C, E], [F, E, D]])))
    # 2면 (N-2) * 4, (N-1) * 4
    face2 = min(list(map(sum, [[A, D], [A, E], [A, C], [A, B], [F, D], [F, B], [F, C], [F, E], [B, D], [D, E], [E, C], [C, B]])))
    # 1면 (N-2)*(N-2), (N-2)*(N-1)*4
    face1 = min([A, B, C, D, E, F])

    answer = (face3*4) + (face2*(4*(N-2)+(N-1)*4)) + (face1*((N-2)*(N-2) + (N-2)*(N-1)*4))
    print(answer)
    return answer


if __name__ == "__main__":
    N0 = int(input())
    dice0 = list(map(int, input().split()))  # ABCDEF
    solution(N0, dice0)
