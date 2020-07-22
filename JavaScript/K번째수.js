function solution(array, commands) {
  var answer = [];

  commands.forEach(command => {
    let newArr = array.slice(command[0]-1, command[1])
    newArr.sort((a, b) => {
      return a-b
    })
    answer.push(newArr[command[2]-1])
  });

  return answer;
}

console.log(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])) // [5, 6, 3]

arr4 = [2,5,3]
arr4.forEach((n) => {
  console.log(n)
})
arr4.sort((a,b) => {
  console.log(a, b)
  return a-b
})