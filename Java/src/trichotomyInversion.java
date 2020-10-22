import java.util.*;

public class trichotomyInversion {
    public static void main(String[] args) {
        int n = 45;

        int answer = 0;
        // 시작
        int mok = 0;
        int nmg = 0;
        ArrayList<Integer> numbers = new ArrayList<>();
        while (n >= 3) {
            mok = (int)(n/3);
            nmg = n%3;
            numbers.add(nmg);
            n = mok;
        }
        numbers.add(mok);
        System.out.println(numbers);
        for (int i=numbers.size()-1; i>=0; i--) {
            answer += numbers.get(i)*(Math.pow(3, numbers.size()-1-i));
        }
        System.out.println(answer);
    }
}
