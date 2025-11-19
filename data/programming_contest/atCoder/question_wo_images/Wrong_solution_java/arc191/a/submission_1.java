import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        String S = scanner.next();
        String T = scanner.next();

        char[] s = S.toCharArray();
        char[] t = T.toCharArray();

        int[] count = new int[10];
        for (int i = 0; i < M; i++) {
            count[t[i] - '0']++;
        }

        for (int i = 9; i > 0; i--) {
            for (int j = 0; j < N && count[i] > 0; j++) {
                if (s[j] < i + '0') {
                    s[j] = (char) (i + '0');
                    count[i]--;
                }
            }
        }

        System.out.println(new String(s));
    }
}