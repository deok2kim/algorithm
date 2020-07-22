function solution(a, b) {
  var answer = 0;
  if (a > b) {
    let tmp = a
    a = b
    b = tmp
  }
  for (let index = a; index <= b; index++) {
    answer += index
    
  }
  return answer;
}

console.log(solution(3, 5))
console.log(solution(3, 3))
console.log(solution(5, 3))