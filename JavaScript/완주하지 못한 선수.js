function solution(participant, completion) {
    var answer = '';
    var success = {}
    participant.forEach((e) => {
        if (!success[e]) {
            success[e] = 1
        } else {
            success[e]++
        }
    })
    completion.forEach((e) => {
        success[e] -= 1
    })
    for (var key in success) {
        if (success[key]) {
            answer = key
            break
        }
    }
    return answer;
}