function solution(n, words) {
    var answer = [0, 0];
    var usedWords = []
    // 한 글자일 경우 시작 할 수 없다.
    if (words[0].length == 1) {
        return [1, 1]
    } else {
        usedWords.push(words[0])
    }
    for (let i = 1; i < words.length; i++) {
        var beforeWord = words[i-1]
        var currentWord = words[i]
        if (beforeWord[beforeWord.length - 1] == currentWord[0]
            && usedWords.indexOf(currentWord) == -1) {
            usedWords.push(currentWord)
        } else {
            var turn = parseInt(i / n) + 1
            var player = i % n + 1
            return answer = [player, turn]
        }
    }
    return answer;
}

console.log(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank'])); // [3,3]