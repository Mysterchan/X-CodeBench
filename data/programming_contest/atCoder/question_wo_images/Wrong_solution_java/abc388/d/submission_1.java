import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] A = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            A[i] = scanner.nextInt();
        }

        int[] B = new int[N + 1];
        System.arraycopy(A, 0, B, 0, N + 1);

        int[] prefixAdults = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            prefixAdults[i] = prefixAdults[i - 1] + (A[i] > 0 ? 1 : 0);
        }

        for (int i = 1; i <= N; i++) {
            int received = prefixAdults[i - 1];
            int given = Math.min(A[i] + received, N - i);
            B[i] = A[i] + received - given;
        }

        for (int i = 1; i <= N; i++) {
            System.out.print(B[i] + " ");
        }
    }
}