'''
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
'''
'''
10
2 3 4 0 0 0 3 4 0 1
0 3 0 4 6 2 4 1 0 5
0 5 0 4 3 1 1 1 1 0
3 5 6 1 4 5 5 2 4 6
1 3 4 0 5 4 0 0 2 0
0 0 6 0 4 4 3 1 0 5
1 6 0 1 3 0 3 0 6 4
0 0 1 4 5 1 3 2 0 6
6 0 5 6 1 1 9 6 0 0
0 4 5 3 6 5 2 1 0 1
'''
from _collections import deque


def eat(food, cnt):
    global baby_shark_location, number_of_moves, number_of_food_eaten, baby_shark_level

    # 리스트를 정렬해주면 제일 위쪽, 제일 왼쪽 순서로 나오게 된다.
    food.sort()
    x, y = food[0][0], food[0][1]

    # 상어를 먹을 물고기의 위치로 옮겨주고
    aquarium[x][y] = 999
    # 기존의 상어 위치를 0으로 바꿔준다.
    aquarium[baby_shark_location[0]][baby_shark_location[1]] = 0
    # 현재 상어의 위치를 저장해주고
    baby_shark_location = [x, y]
    # 총 이동횟수를 +cnt만큼, 먹은 물고기 수를 +1만큼 해준다.
    number_of_moves += cnt
    number_of_food_eaten += 1

    # 만약 상어의 레벨과 물고기를 먹은 수가 같을 경우 레벨업!
    if number_of_food_eaten == baby_shark_level:
        baby_shark_level += 1
        number_of_food_eaten = 0

    return


# 먹을 수 있는 물고기 찾기 - 있다면 1마리 or more
def hunt(location):
    global baby_shark_level

    dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]  # 상 좌 우 하 | 거리가 똑같을 때 먼저 먹는 순서
    visit_aquarium = [[0]*n for _ in range(n)]  # 탐색을 했는지 않했는지

    q = deque()
    q.append([location[0], location[1]])
    # 먹을 수 있는 물고기가 들어갈 리스트, 그 음식까지의 거리
    foods = []
    food_distance_check = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visit_aquarium[nx][ny]:
                # 만약 물고기가 없거나, 상어와 레벨이 같으면 이동통로가 된다
                if aquarium[nx][ny] == 0 or aquarium[nx][ny] == baby_shark_level:
                    visit_aquarium[nx][ny] += visit_aquarium[x][y] +1
                    q.append((nx, ny))
                # 상어의 레벨보다 작으면 위치를 foods에 저장
                elif aquarium[nx][ny] < baby_shark_level:
                    visit_aquarium[nx][ny] += visit_aquarium[x][y] + 1

                    # foods에 처음으로 물고기가 저장되면 그 물고기 까지의 거리를 나타내주고
                    if not foods:
                        food_distance_check = visit_aquarium[nx][ny]

                    # 그 이후에는 그 거리 이상의 먹을 수 있는 물고기는 저장하지 않는다.
                    else:
                        # 만약 먹을 수 있는 물고기보다 더 먼 곳에 있는 물고기를 탐색하기 시작한다면 eat함수 실행
                        if visit_aquarium[nx][ny] > food_distance_check:
                            eat(foods, food_distance_check)
                            return False

                    foods.append((nx, ny))
    else:
        # 가장 먼 물고기들만 먹을 수 있는 경우 위의 조건이 실행되지 않기 때문에 여기서 다시한번 eat함수 실행
        if foods:
            eat(foods, food_distance_check)
            return False

    return True


n = int(input())
aquarium = [list(map(int, input().split())) for _ in range(n)]

# 총 이동 횟수, 각 레벨에서 물고기를 먹은 수, 현재 상어 레벨
number_of_moves = 0
number_of_food_eaten = 0
baby_shark_level = 2

# 현재 위치 찾기
baby_shark_location = ''
for i in range(n):
    for j in range(n):
        if aquarium[i][j] == 9:
            # 레벨이 9를 넘을 수 있으므로 바꿔줌
            aquarium[i][j] = 999
            baby_shark_location = [i, j]
            break

# while문 반복, 먹을 물고기가 없을 경우 bre ak
while True:
    if hunt(baby_shark_location):
        break
    # print(baby_shark_location, 'lv:', baby_shark_level, 'move:', number_of_moves, 'eat:', number_of_food_eaten)
    # for row in aquarium:
    #     print(row)
    # print()

print(number_of_moves)
