function solution(jobs) {
    var answer = 0;
    const N = jobs.length

    // jobs 거꾸로 정렬
    jobs.sort((a,b)=>{
        if (a[0] > b[0]) return -1
        if (a[0] < b[0]) return 1
        if (a[1] > b[1]) return -1
        if (a[1] > b[1]) return 1
    })
    // console.log(jobs)
    // 큐
    let q = []
    let now_time = 0
    do {
        // 현재시간보다 입장시간이 적은 작업들 집어 넣기
        let idx = jobs.length - 1
        while (jobs.length>0) {
            if (jobs[idx][0] <= now_time) {
                enq(jobs[idx][0], jobs[idx][1])
                jobs.pop()
                idx --
            } else {
                break
            }
        }
        // q에 작업이 없고 jobs에만 작업이 있다면
        if (q.length == 0 && jobs.length > 0) {
            const new_work = jobs[jobs.length - 1]
            enq(new_work[0], new_work[1])
            jobs.pop()
            now_time = new_work[0]
        }
        // 맨 앞의 작업 하나 빼기 (작업하기)
        // console.log('큐', q)
        const work = q.shift()
        // console.log(now_time, work)
        const enter_time = work[0]
        const work_time = work[1]
        answer += now_time - enter_time + work_time
        now_time += work_time

    }
    while (q.length > 0 || jobs.length > 0)
    // d: data(enter_time), p: priority(work_time)
    function enq(d, p) {
        let idx = 0
        for (let j = 0; j<q.length; j++) {
            if ( p < q[j][1] && q[j][1] < q[idx][1]) {
                idx = j
            }
        }
        q.splice(idx, 0, [d,p])
    }
    return Math.floor(answer/N);
}

console.log(solution([[0, 3], [1, 9],[31, 5], [2, 6],[30, 3], [30, 5], [55,10]]))