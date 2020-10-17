function solution(strings, n) {
    strings.sort((a, b) => {
        // a의 n번째와 b의 n 번째가 같으면
        // a와 b를 비교
        // 다르면
        // a의 n번쨰와 b의 n 번째를 비교
        return a[n] === b[n] ? a.localeCompare(b) : a[n].localeCompare(b[n])
    })
    return strings
}