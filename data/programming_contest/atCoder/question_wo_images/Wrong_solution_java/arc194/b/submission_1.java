import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] P = new int[N];
        for (int i = 0; i < N; i++) {
            P[i] = scanner.nextInt();
        }
        long ans = 0;
        for (int i = 0; i < N; i++) {
            if (P[i] != i + 1) {
                for (int j = i + 1; j < N; j++) {
                    if (P[j] == i + 1) {
                        for (int k = j; k > i; k--) {
                            int temp = P[k];
                            P[k] = P[k - 1];
                            P[k - 1] = temp;
                            ans += k;
                        }
                        break;
                    }
                }
            }
        }
        System.out.println(ans);
    }
}