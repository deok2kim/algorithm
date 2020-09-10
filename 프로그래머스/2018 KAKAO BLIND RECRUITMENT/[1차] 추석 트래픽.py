
def solution(lines):
    print('케이스')
    answer = []

    times = []
    for line in lines:
        time,second = line.split()[1:]
        # print(time, second)

        time = list(map(float, time.split(':')))
        print(time)
        end = time[0]*60*60 + time[1]*60 + time[2]
        print(end)
        second = float(second[:-1])
        print(second)
        end *= 1000
        second *= 1000
        start = end - second + 1
        print(int(start) ,'~', int(end))
        times.append([int(start), int(end)])


        print()
    print(times)

    for i in range(len(times)):
        print('-------------------------',i+1)
        a = times[i][0]
        b = times[i][1]
        cnt = 0
        print(a)
        for j in range(len(times)):
            if times[j][0] <= a <= times[j][1]:
                print('앞')
                cnt+= 1
            elif a <= times[j][0] <= a+999:
                print('앞??')
                cnt += 1
            else:
                answer.append(cnt)
        cnt = 0
        print(b)
        for j in range(len(times)):
            if times[j][0] <= b <= times[j][1]:
                print('뒤')
                cnt+= 1
            elif b <= times[j][0] <= b+999:
                print('뒤??')
                cnt += 1
            else:
                answer.append(cnt)
        else:
            answer.append(cnt)
    answer = max(answer)
    return answer


# print(solution(['2016-09-15 01:00:04.001 2.0s', '2016-09-15 01:00:07.000 2s']))
# print(solution(['2016-09-15 01:00:04.002 2.0s', '2016-09-15 01:00:07.000 2s']))
print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))
