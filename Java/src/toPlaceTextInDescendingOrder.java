import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

public class toPlaceTextInDescendingOrder {
    public static void main(String[] args) {
        String s = "shfjkshdfushdfjashHDASFUSDFHsjdhfjksUDZHf";
        String answer = "";

        // 시작
        String[] result = s.split("");
        System.out.println(Arrays.toString(result));
        Arrays.sort(result, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o2.compareTo(o1);

            }

            ;
        });
//        Arrays.sort(result, Collections.reverseOrder());

        System.out.println(Arrays.toString(result));
        String a = String.join("", result);
        System.out.println(a);

    }
}
