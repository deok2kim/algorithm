function solution(s) {
    var answer = '';
    var s_array = s.split('')

    s_array.sort((a, b) => {
        return a < b ? 1 : a > b ? -1 : 0
    })
    console.log(s_array)
    answer = s_array.join("")
    return answer
}