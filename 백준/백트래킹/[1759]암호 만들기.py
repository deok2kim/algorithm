def bt(idx, word):
    # 암호의 길이가 L이 됐을 때
    if len(word) == L:
        vowel_cnt = 0
        consonant_cnt = 0
        for w in word:
            if w in vowel:
                vowel_cnt += 1
            else:
                consonant_cnt += 1

            # 자음이 1개 이상, 모음이 2개 이상일 때만 result에 추가해 준다.
            if vowel_cnt >= 1 and consonant_cnt >= 2:
                result.add(word)
                break

        return

    # 함수에 들어갈 때 이전 선택 다음부터 선택: i+1
    for i in range(idx, C):
        bt(i+1, word+words[i])


L, C = map(int, input().split())
words = input().split()

# 문제에서 암호는 알파벳이 증가하는 순서 대로 짜야 하므로
words.sort()

# 모음의 포함 유무 확인용
vowel = 'aeiou'

# 중복된 결과 선택을 피하기 위해 set 사용
result = set()
bt(0, '')

# set은 순서가없으므로 list로 바꿔준 후 정렬
result = list(result)
result.sort()
for row in result:
    print(row)
