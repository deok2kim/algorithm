function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    let on_the_bridge = []
    let trucks_time = []
    let total_weight = 0
    do {
        // 다리 위에 있는 트럭 1초씩 빼주기
        for (let i in trucks_time) {
            trucks_time[i]--
        }

        // 다리 위에 있는 맨 앞 트럭의 시간이 0초면 다리 위에서 트럭 제거
        if (trucks_time[0] == 0) {
            trucks_time.shift()
            total_weight -= on_the_bridge.shift()
        }

        // 다리에 자리가 남고, 무게도 남을 때 트럭 넣기
        if (on_the_bridge.length < bridge_length && total_weight + truck_weights[0] <= weight) {
            var truck = truck_weights.shift()
            total_weight += truck
            on_the_bridge.push(truck)
            trucks_time.push(bridge_length)
        }
        answer++
    } while (on_the_bridge.length > 0)
    return answer;
}