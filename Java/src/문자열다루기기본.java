public class 문자열다루기기본 {
    public static void main(String[] args) {
        String s = "1234";

        if (s.length() == 4 || s.length() == 6) {
            for(int i = 0; i < s.length(); i++) {
                if (!Character.isDigit(s.charAt(i))) {
                    System.out.println("거짓");
                }
            }
        }
    }
}
