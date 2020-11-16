import java.util.*;

public class 수건돌리기게임 {
    public static void main(String[] args) {
        int numOfAllPlayers = 6;
        int numOfQuickPlayers = 2;
        char[] namesOfQuickPlayers = {'B', 'C'};
        int numOfGames = 2;
        int[] numOfMovesPerGame = {3, -2};

        // 시작
        // 66부터
        char[] ground = new char[numOfAllPlayers];
        for (int i = 0; i < ground.length - 1; i++) {
            ground[i] = (char)(66+i);
        }
        System.out.println(ground);
        HashMap<Character, Integer> visited = new HashMap<>();
        for(char player: ground) {
            visited.put(player, 0);
        }
        char soolae = 'A';
        visited.put(soolae, 1);
        System.out.println(visited.get("A"));

        int idx = 0;
        for (int i=0; i< numOfMovesPerGame.length; i++) {
            idx += numOfMovesPerGame[i];
            if (idx >= numOfAllPlayers - 1) {
                idx = idx % (numOfAllPlayers - 1);
            }
            if (idx < 0) {
                idx = Math.abs(idx) % (numOfAllPlayers - 1);
                idx = numOfAllPlayers - 1 - idx;
            }
            System.out.println("이동");
            System.out.println(idx);
            System.out.println("새로운 술래");
            char new_soolae = ground[idx];
            // 술래가 되면 + 1

            System.out.println(new_soolae);
            boolean q = false; // 다시 잡혔는지
            for (char quick: namesOfQuickPlayers){
                if (quick == new_soolae) {
                    // 다시 술래가 된다.
                    q = true;
                    break;
                }
            }
            if (q) {
                // 다시 잡혔으면 위치 안바뀌고 술래도 안바뀜
                System.out.println("잡힙");

                visited.put(soolae, visited.get(soolae) + 1);
            } else {
                // 다시 안잡히면 위치바뀌고 술래바뀜
                visited.put(new_soolae, visited.get(new_soolae) + 1);
                System.out.println("안잡힙");
                ground[idx] = soolae;
                soolae = new_soolae;
            }
            System.out.println(ground);
        }
        // 결과
        System.out.println("결과");
        for (int k = 0; k< ground.length-1; k++) {
            System.out.printf("%c %d", ground[k], visited.get(ground[k]));
            System.out.println("");
        }
        System.out.printf("%c %d", soolae, visited.get(soolae));
    }
}
