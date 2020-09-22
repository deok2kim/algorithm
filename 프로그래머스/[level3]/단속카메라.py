def solution(routes):
    answer = 1
    routes.sort()

    camera = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] <= camera:
            camera = min(camera, routes[i][1])
        else:
            camera = routes[i][1]
            answer += 1
    return answer


qq = [
    [[-20, 15], [-14, -5], [-18, -13], [-11, -3]]
]

for q in qq:
    print(solution(q))
