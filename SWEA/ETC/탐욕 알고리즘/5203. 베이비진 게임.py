for tc in range(int(input())):
    cards = list(map(int, input().split()))

    player1 = [0]*10
    player2 = [0]*10

    result = 0
    for i in range(len(cards)):
        if i % 2 == 0:
            player1[cards[i]] += 1

        else:
            player2[cards[i]] += 1

        # check
        for idx in range(len(player1)):
            if player1[idx] >= 3:
                result = 1
                break

            if player2[idx] >= 3:
                result = 2
                break

            if idx <= 7:
                if player1[idx] >= 1 and player1[idx + 1] >= 1 and player1[idx + 2] >= 1:
                    result = 1
                    break

                if player2[idx] >= 1 and player2[idx + 1] >= 1 and player2[idx + 2] >= 1:
                    result = 2
                    break

        if result > 0:
            break
    print('#{} {}'.format(tc+1, result))
