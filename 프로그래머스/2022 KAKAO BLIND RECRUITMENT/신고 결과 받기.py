def solution(id_list, report, k):
    answer = []
    reported_dict = {id: {'reporter': set(), 'mail_cnt': 0} for id in id_list}

    for r in report:
        reporter, reported_person = r.split(' ')
        reported_dict[reported_person]['reporter'].add(reporter)

    for key, val in reported_dict.items():
        if len(val['reporter']) >= k:
            for reporter in reported_dict[key]['reporter']:
                reported_dict[reporter]['mail_cnt'] += 1

    for val in reported_dict.values():
        answer.append(val['mail_cnt'])
    return answer


print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2))
