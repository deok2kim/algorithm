function solution(board, moves) {
    var answer = 0;
    var n = board.length
    // board.forEach((e)=>{
    //     console.log(e)
    // })
    // console.log()
    var new_board = []
    for (var j = 0; j < n; j++) {
        var tmp_line = []
        for (var i = n - 1; i >= 0; i--) {
            tmp_line.push(board[i][j])
        }
        new_board.push(tmp_line)
    }
    // new_board.forEach((e)=>{
    //     console.log(e)
    // })

    var box = []
    moves.forEach((e) => {
        while (new_board[e - 1].length > 0) {
            var doll = new_board[e - 1].pop()
            if (doll != 0) {
                if (box.length > 0 & box[box.length - 1] == doll) {
                    box.pop()
                    answer++

                } else {
                    box.push(doll)
                }
                break
            }
        }
        // console.log(box)
        // console.log(answer)
    })


    // new_board.forEach((e)=>{
    //     console.log(e)
    // })
    return answer * 2;
}