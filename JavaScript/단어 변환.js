function solution(begin, target, words) {
    var answer = 0;
    // 타겟이 워드에 없는 경우
    if (!words.includes(target)) {
        return answer
    }

    let n = words.length
    // visited 와 queue
    let visited = Array(n).fill(0)
    let q = [begin]

    // 단어의 인덱스를 객체에 저장
    const words_obj = {}
    for (let i in words) {
        words_obj[words[i]] = i
    }

    while (q.length > 0) {
        let c = q.shift()

        // 타겟 워드에 도달하면 끝
        if (c == target) {
            return visited[words_obj[c]]
        }
        for (let i in words) {
            if (visited[i] == 0) {
                let word = words[i]
                let diff = 0
                for (let j in word) {
                    if (c[j] != word[j]) {
                        diff++
                    }
                    if (diff > 1) {
                        break
                    }
                }
                if (diff == 1) {
                    q.push(word)
                    if (c == begin) {
                        visited[i] = 1
                    } else {
                        visited[i] = visited[words_obj[c]] + 1
                    }

                }
            }

        }
    }

    console.log(visited)
    return answer;
}