import java.util.*;

public class splittingNumbericalArray {
    public static void main(String[] args) {
        int[] arr = {5, 9, 7, 10};
        int divisor = 5;


        // 시작
        ArrayList<Integer> result = new ArrayList<>();
        for (int num : arr) {
            if (num % divisor == 0) {
                result.add(num);
            }
        }
        System.out.println(result);
        if (result.size() == 0) {
            int[] answer = {-1};
            System.out.println(answer);
        } else {
            int[] answer = new int[result.size()];
            for (int i = 0; i < answer.length; i++) {
                answer[i] = result.get(i);
            }
            Arrays.sort(answer);
            System.out.println(answer);
        }

    }
}
