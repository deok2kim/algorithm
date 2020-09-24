def solution(genres, plays):
    answer = []
    n = len(genres)
    album = {}
    for i in range(n):
        if album.get(genres[i]):
            album[genres[i]]['cnt'] += plays[i]
            album[genres[i]]['songs'].append((plays[i], i))
        else:
            #
            album[genres[i]] = {
                'cnt': plays[i],
                'songs': [(plays[i], i)]
            }

    # print(album)

    for key, value in album.items():
        # print(key)
        # print(value['songs'])
        album[key]['songs'] = sorted(value['songs'], key=lambda x: (-x[0], x[1]))
    ordered_album = sorted(album.items(), key=lambda x: -x[1]['cnt'])
    # print(ordered_album)
    for row in ordered_album:
        songs = row[1]['songs']
        # print(songs)
        for idx in range(len(songs)):
            if idx < 2:
                answer.append(songs[idx][1])
    # print(answer)
    return answer


print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500], ))  # [4, 1, 3, 0]
