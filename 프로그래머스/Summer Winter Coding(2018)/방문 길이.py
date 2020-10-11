def solution(dirs):
    answer = 0
    n = 11

    maps = [[0]*n for _ in range(n)]
    # for row in maps:
    #     print(row)

    visited = set()

    #UDRL
    move = {
        'U': [-1, 0],
        'D': [1, 0],
        'L': [0,-1],
        'R': [0,1],
    }
    x, y = 5, 5
    for d in dirs:
        dx, dy = move[d]
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            visited.add((x,y,nx,ny))
            visited.add((nx,ny,x,y))
            x,y = nx,ny

    # print(visited)
    # print(len(visited))
    answer = len(visited)//2





    return answer


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))