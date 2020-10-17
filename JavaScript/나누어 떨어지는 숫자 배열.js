function solution(arr, divisor) {
    var answer = [];
    arr.forEach(e => {
        if (e % divisor == 0) {
            answer.push(e)
        }
    })
    if (answer.length > 0) {
        answer.sort((a, b) => {
            return a - b
        })
    } else {
        answer = [-1]
    }

    return answer;
}