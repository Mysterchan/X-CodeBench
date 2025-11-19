import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] A = new int[N];
        int[] B = new int[M];

        for (int i = 0; i < N; i++)
            A[i] = sc.nextInt();

        for (int i = 0; i < M; i++)
            B[i] = sc.nextInt();

        int left = -1, right = -1;
        int idx = 0;

        for (int l = 0; l < N; l++) {
            if (A[l] == B[idx]) {
                idx++;

                if (idx == M) {
                    left = l - (M - 1);
                    break;
                }
            } else {
                idx = 0;
            }
        }

        idx = 0;

        for (int r = N - 1; r >= 0; r--) {
            if (A[r] == B[M - 1 - idx]) {
                idx++;

                if (idx == M) {
                    right = r;
                    break;
                }
            } else {
                idx = 0;
            }
        }

        if (left == -1) {
            System.out.println(-1);
        } else {
            System.out.println((left < right) ? "Yes" : "No");
        }
    }
}