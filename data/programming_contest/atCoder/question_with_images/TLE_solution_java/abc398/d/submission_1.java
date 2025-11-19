import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int R = sc.nextInt();
        int C = sc.nextInt();
        String S = sc.next();

        ArrayList<int[]> list = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            char c = S.charAt(i);
            if (c == 'E') {
                for (int[] ints : list) ints[1]++;
                list.add(new int[]{0, 1});
            } else if (c == 'W') {
                for (int[] ints : list) ints[1]--;
                list.add(new int[]{0, -1});
            } else if (c == 'S') {
                for (int[] ints : list) ints[0]++;
                list.add(new int[]{1, 0});
            } else if (c == 'N') {
                for (int[] ints : list) ints[0]--;
                list.add(new int[]{-1, 0});
            }

            boolean flag = false;
            for (int[] ints : list) {
                if (ints[0] == R && ints[1] == C) {
                    flag = true;
                    break;
                }
            }
            sb.append(flag ? 1 : 0);
        }
        System.out.println(sb.toString());
    }
}