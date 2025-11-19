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
        int[] prefixSum = new int[N + 1];
        int totalAdults = 0;

        for (int i = 1; i <= N; i++) {
            B[i] = A[i] + totalAdults;
            if (A[i] > 0) {
                totalAdults++;
            }
        }
        B = new int[N + 1];
        int[] C = new int[N + 1];
        System.arraycopy(A, 0, C, 0, N + 1);

        for (int year = 1; year <= N; year++) {
            int newAdult = year;
            int gifts = 0;
            for (int i = 1; i < year; i++) {
                if (C[i] > 0) {
                    gifts++;
                    C[i]--;
                }
            }
            C[newAdult] += gifts;
        }

        for (int i = 1; i <= N; i++) {
            B[i] = C[i];
        }
        int[] prefixAdults = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            prefixAdults[i] = prefixAdults[i - 1] + (A[i] > 0 ? 1 : 0);
        }

        for (int i = 1; i <= N; i++) {
            int received = prefixAdults[i - 1];
            int given = Math.min(A[i] + received, N - i);
            B[i] = A[i] + received - given;
        }

        B = new int[N + 1];
        System.arraycopy(A, 0, B, 0, N + 1);

        for (int year = 1; year <= N; year++) {
            int newAdult = year;
            int gifts = 0;
            for (int i = 1; i < year; i++) {
                if (B[i] > 0) {
                    gifts++;
                    B[i]--;
                }
            }
            B[newAdult] += gifts;
        }
        for (int i = 1; i <= N; i++) {
            System.out.print(B[i] + " ");
        }
    }
}