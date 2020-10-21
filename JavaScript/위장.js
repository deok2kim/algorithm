function solution(clothes) {
    var answer = 0;
    let clothes_dict = {}
    for (let i in clothes) {
        let name = clothes[i][0]
        let type = clothes[i][1]
        if (clothes_dict[type]) {
            clothes_dict[type]++
        } else {
            clothes_dict[type] = 1
        }
    }

    // +1을 해주는 이유는 선택을 안하는 경우 포함
    let result = 1
    Object.values(clothes_dict).forEach((e) => {
        result *= (e + 1)
    })
    answer = result - 1
    return answer;
}