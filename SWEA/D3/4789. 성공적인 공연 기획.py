for tc in range(int(input())):
    sequence = input()
    people = 0
    employment = 0
    for need_people, people_cnt in enumerate(sequence):
        people_cnt = int(people_cnt)
        if need_people <= people:
            people += people_cnt
        else:
            employment += need_people - people
            people += need_people - people + people_cnt

    print(f'#{tc + 1} {employment}')
