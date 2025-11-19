import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] A = new int[N];
        int[] B = new int[M];
        int[] left = new int[M];
        int[] right = new int[M];

        for (int i = 0; i < N; i++)
            A[i] = sc.nextInt();

        for (int i = 0; i < M; i++)
            B[i] = sc.nextInt();

        int idx = 0;

        for (int l = 0; l < N && idx < M; l++) {
            if (A[l] == B[idx]) {
                left[idx] = l;
                idx++;
            }
        }

        if (idx < M) {
            System.out.println("No");
            return;
        }

        idx = M - 1;

        for (int r = N - 1; r >= 0 && idx >= 0; r--) {
            if (A[r] == B[idx]) {
                right[idx] = r;
                idx--;
            }
        }

        boolean ok = false;
        for (int i = 0; i < M; i++) {
            if (left[i] < right[i]) {
                ok = true;
                break;
            }
        }

        System.out.println(ok ? "Yes" : "No");
    }
}