function solution(skill, skill_trees) {
    var answer = 0;

    for (var i = 0; i < skill_trees.length; i++) {
        var skill_idx = 0
        for (var j = 0; j < skill_trees[i].length; j++) {
            var c = skill_trees[i][j]
            if (skill[skill_idx] == c) {
                skill_idx++
            } else if (skill.includes(c)) {
                skill_idx = -1
                break
            }
        }
        if (skill_idx != -1) {
            answer++
        }
    }
    return answer;
}