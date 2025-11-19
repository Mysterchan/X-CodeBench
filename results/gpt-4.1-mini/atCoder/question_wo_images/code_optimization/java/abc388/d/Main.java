import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] A = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            A[i] = scanner.nextInt();
        }

        // prefixAdults[i] = number of adults with stones among aliens 1..i
        int[] prefixAdults = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            prefixAdults[i] = prefixAdults[i - 1] + (A[i] > 0 ? 1 : 0);
        }

        int[] result = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            int received = prefixAdults[i - 1]; // gifts received from adults before i
            int maxGiftsGiven = N - i;          // max gifts alien i can give after becoming adult
            int given = Math.min(A[i] + received, maxGiftsGiven);
            result[i] = A[i] + received - given;
        }

        for (int i = 1; i <= N; i++) {
            System.out.print(result[i] + (i == N ? "\n" : " "));
        }
    }
}