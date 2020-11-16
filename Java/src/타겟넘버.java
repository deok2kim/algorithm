//public class 타겟넘버 {
//    public static void main(String[] args) {
//        int[] numbers = {1,1,1,1,1};
//        int target = 3;
//
//        // 시작
//        int answer = 0;
//
//
//
//        int result = dfs(numbers, target,0,0);
//
//    }
//    public static int dfs(int[] numbers,int target int idx, int total) {
//        System.out.println(idx);
//        if (idx == numbers.length) {
//            if (total == target) {
//                return 1;
//            }
//            return 0;
//        }
//
//        dfs(numbers,target, idx+1, total+numbers[idx]);
//        dfs(numbers,target,idx+1, total-numbers[idx]);
//    };
//}
