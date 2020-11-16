public class sumBetweenTwoIntegers {
    public static void main(String[] args) {
        int a = 3;
        int b = 3;
        long answer = 0;

        // 시작
        if (a>b) {
            int tmp = a;
            a = b;
            b = tmp;
        }

        for (int i=a; i<=b; i++) {
            answer += i;
        }
        System.out.println(answer);
    }
}
