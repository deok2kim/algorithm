function solution(citations) {
    var answer = 0;
    let n = citations.length
    citations.sort((a, b) => {
        return a - b
    })

    console.log(citations)
    for (let i = 0; i < n; i++) {
        if (citations[i] >= n - i) {
            return n - i
        }
    }
    return answer;
}