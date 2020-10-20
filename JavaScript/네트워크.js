function solution(n, computers) {
    var answer = 0;

    let visited = Array(n).fill(0)
    let stack = []
    for (let i = 0; i < n; i++) {
        if (visited[i] == 0) {
            stack.push(i)
            visited[i] = 1
            while (stack.length > 0) {
                let c = stack.shift()
                for (let j in computers[c]) {
                    if (computers[c][j] == 1 && visited[j] == 0) {
                        stack.push(j)
                        visited[j] = 1
                    }
                }
            }
            answer++
        }
    }
    return answer;
}