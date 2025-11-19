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
        int totalAdults = 0;

        for (int i = 1; i <= N; i++) {
            B[i] = A[i] + totalAdults;
            if (A[i] > 0) {
                totalAdults++;
            }
            // Calculate how many stones will be given away
            if (i > 1) {
                int gifts = Math.min(totalAdults - 1, A[i]);
                B[i] -= gifts;
            }
        }

        // Adjust the stones for each alien based on the gifts received
        for (int i = 1; i <= N; i++) {
            if (i < N) {
                B[i + 1] += Math.max(0, B[i]);
            }
        }

        for (int i = 1; i <= N; i++) {
            System.out.print(B[i] + " ");
        }
    }
}