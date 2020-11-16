public class numberOfPAndYInString {
    public static void main(String[] args) {
        String s = "pPoooyY";
        boolean answer = true;

        int cnt = 0;
        for(int i = 0; i<s.length(); i++) {
            String tmp = s.substring(i,i+1).toLowerCase();

            if (tmp.equals("y")) {
                cnt ++;

            }
            if (tmp.equals("p")) {
                cnt --;
            }

        }
        if (cnt != 0) {
            answer = false;
        }
        System.out.println(answer);
    }
}
