import java.util.*;

public class toSortFreelyWithinAString {
    public static void main(String[] args) {
//        String[] strings = {"sun", "bed", "car"};
//        int n = 1;
        String[] strings = {"abce", "abcd", "cdx"};
        int n = 2;

        // 시작
        Arrays.sort(strings, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                if (s1.charAt(n) > s2.charAt(n)) {
                    return 1;
                } else if (s1.charAt(n) < s2.charAt(n)) {
                    return -1;
                } else {
                    if (s1.compareTo(s2) > 0) {
                        return 1;
                    } else {
                        return -1;
                    }
                }
            }
        });
        for (String s: strings) {
            System.out.println(s);
        }
        String a = "asDF";
        System.out.println(a.charAt(0));
        System.out.println(a.charAt(1));
        System.out.println(a.charAt(0) > a.charAt(1));
        a.toLowerCase();
        System.out.println(a);
    }
}
