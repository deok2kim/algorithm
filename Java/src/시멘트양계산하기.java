import java.util.Arrays;

public class 시멘트양계산하기 {
    public static void main(String[] args) {
        int day = 2;
        int width = 6;
        int[][] blocks = {
                {6, 2, 11, 0, 3, 5},
                {6, 3, 0, 9, 0, 5}
        };

        int answer = 0;
        // 시작
        int[] ground = new int[width];
        // 날짜 시작
        for (int i = 0; i < day; i ++) {
            // 벽돌 쌓기
            for (int j=0; j<width; j ++) {
                ground[j] += blocks[i][j];
            }
            System.out.println("벽돌쌓기");
            System.out.println(Arrays.toString(ground));

            // 시멘트 붓기
            for (int j=1; j<width-1; j++) {
                int left = j-1;
                int right = j+1;

                // 양 벽중 하나가 현재보다 작으면 씨멘트 못함 오른쪽은 같아도 종료
                if (ground[left] < ground[j] || ground[right] <= ground[j]) {
                    continue;
                }

                // 만약 왼쪽이 더 크면 오른쪽 만큼 쌓고 종료
                if (ground[left] >= ground[right]) {
                    answer += ground[right] - ground[j];
                    ground[j] = ground[right];
                    continue;
                } else { // 오른쪽이 더 큰 상황
                    int same_zone = left;
                    // 왼쪽 확인 더 쌓으러 갈 수 있는지 확인
                    while (left > 0) {
                        // 왼쪽으로 한칸 더 가보자
                        left -= 1;
                        // 왼쪽이 오른쪽보다 더 크다.
                        if (ground[left] >= ground[right]) {
                            for(int l=left+1; l<right; l++) {
                                answer += ground[right] - ground[l];
                                ground[l] = ground[right];

                            }
                            break;

                        }
                        // 왼쪾이 바로 전보다 낮아짐
                        if (ground[left] < ground[left+1]) {
                            for(int l=left+2; l<right; l++) {
                                answer += ground[left+1] - ground[l];
                                ground[l] = ground[left+1];

                            }
                            break;
                        }

                        // 왼쪽 끝에 도착
                        // j랑 맨 끝이랑 같으면 시멘트 못함
                        if (left == 0) {
                            if (ground[left] == ground[j]) {
                                System.out.println("혹시여기?");
                                break;
                            } else {
                                for(int l=left+1; l<right; l++) {
                                    answer += ground[left] - ground[l];
                                    ground[l] = ground[left];

                                }
                                break;
                            }
                        }
                    }
                }



            }
            System.out.println("시멘트붓기");
            System.out.println(Arrays.toString(ground));
            System.out.println(answer);

        }

    }
}

