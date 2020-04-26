from itertools import combinations

n, m = map(int, input().split())
village = [list(map(int, input().split())) for _ in range(n)]

chicken_house_all = []
home_sweet_home = []
for i in range(n):
    for j in range(n):
        if village[i][j] == 2:
            chicken_house_all.append((i, j))
            village[i][j] = 0
        elif village[i][j] == 1:
            home_sweet_home.append((i,j))

# print(chicken_house_all)
chicken_house_combi = list(combinations(chicken_house_all, m))
# print(chicken_house_combi)

distance_list = []
while chicken_house_combi:
    chicken_house_choice = chicken_house_combi.pop()
    for i, j in chicken_house_choice:
        village[i][j] = 2

    distance = 0
    for r1, c1 in home_sweet_home:
        tmp = []
        for r2, c2 in chicken_house_choice:
            tmp.append(abs(r1-r2) + abs(c1-c2))

        distance += min(tmp)

    distance_list.append(distance)

# print(distance_list)
print(min(distance_list))

