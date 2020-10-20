function solution(numbers) {
    var answer = 0;
    let results = new Set()
    const N = numbers.length

    // 퍼뮤 펑션
    let visited = Array(N).fill(false)
    const permu = function (arr, C) {
        if (arr.length == C) {
            let num = parseInt(arr)
            if (num >= 2) {
                results.add(num)
            }
            return
        }
        for (let j = 0; j < N; j++) {
            if (!visited[j]) {
                visited[j] = !visited[j]
                permu(arr + numbers[j], C)
                visited[j] = !visited[j]
            }
        }
    }

    for (let i = 1; i < N + 1; i++) {
        permu('', i)
    }

    // 프라임 펑션
    const prime = function (num) {
        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false
            }
        }
        return true
    }

    results.forEach(e => {
        if (prime(e)) {
            answer++
        }
    })
    return answer;
}