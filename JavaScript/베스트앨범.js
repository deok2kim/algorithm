function solution(genres, plays) {
  var answer = [];
  var chart = {}
  // 인풋값 객체화
  for (let i = 0; i < genres.length; i++) {
    if (!chart[genres[i]]) {
      chart[genres[i]] = {
        playCount: plays[i],
        index: [[plays[i], i]]
      }
    } else {
      chart[genres[i]].playCount += plays[i]
      chart[genres[i]].index.push([plays[i], i])
    }
  }
  
  // 객체 정렬
  var sorted = Object.values(chart).sort((l, r) => r.playCount - l.playCount);
  // 정렬 후 각각의 장르에서 노래들을 정렬
  sorted.forEach(genre => {
    if (genre.index.length > 1) {
      genre.index.sort((a,b) => {
        if (a[0] > b[0]) {
          return -1;
        } else if (a[0] < b[0]) {
          return 1;
        } else {
          if (a[1] > b[1]) {
            return 1
          } else {
            return -1
          }
        }
      })
      answer.push(genre.index[0][1])
      answer.push(genre.index[1][1])
    } else {
      answer.push(genre.index[0][1])
    }
  });

  return answer;
}

console.log(solution(["classic", "pop", 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500])); // [4, 1, 3, 0]