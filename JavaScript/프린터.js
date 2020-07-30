function solution(priorities, location) {
    var answer = 0;
    // 인쇄를 몇번 했는지
    var cnt = 0
    // 내문서의 위치
    var myDoc = location
    while (priorities.length > 0) {
        // 맨 앞의 문서를 꺼낸다
        var c = priorities.shift()
        // 만약 맨앞의 문서의 우선순위보다 높은 문서가 존재한다면
        if (priorities.filter((e) => e > c).length > 0) {
            // 인쇄를 하지 않고 배열의 맨 뒤에 넣는다.
            priorities.push(c)
            // 맨앞의 문서의 우선순위보다 높은 문서가 없다면
        } else {
            // 인쇄 카운트를 올려주고
            cnt ++
            // 그게 바로 내문서라면 
            if (myDoc == 0) {
                // 함수를 종료하고 cnt를 리턴한다.
                return answer = cnt
            }
        }
        // 문서를 하나 꺼낼 때마다 내문서의 위치를 하나씩 줄여간다
        myDoc --
        // 만약 내문서가 맨뒤로 갔다면
        if (myDoc === -1) {
            // 내문서 위치인덱스도 맨뒤로 바꿔준다.
            myDoc = priorities.length - 1
        }
    }
    return answer;
}


console.log(solution([2, 1, 3, 2], 2))
console.log(solution([1, 1, 9, 1, 1, 1], 0))