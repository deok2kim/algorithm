function solution(progresses, speeds) {
  var answer = [];
  
  while (progresses.length > 0) {
    var cnt = 0
    for (let i = 0; i < progresses.length; i++) {
      progresses[i] += speeds[i]
    }

    while (1) {
      if (progresses[0] >= 100) {
        progresses.splice(0, 1)
        speeds.splice(0, 1)
        cnt ++
      } else {
        break
      }
    }
    if (cnt > 0) {
      answer.push(cnt)
    }
  }
  return answer;
}

console.log(solution([93,30,55]	,[1,30,5]	))