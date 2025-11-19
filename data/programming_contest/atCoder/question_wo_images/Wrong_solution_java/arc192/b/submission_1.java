import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] A = new int[N];
        long sum = 0;
        for (int i = 0; i < N; i++) {
            A[i] = scanner.nextInt();
            sum += A[i];
        }
        long k = (sum - N) / N;
        long cnt = 0;
        for (int i = 0; i < N; i++) {
            if (A[i] > k + 1) {
                cnt++;
            }
        }
        if (cnt % 2 == 1) {
            System.out.println("Fennec");
        } else {
            System.out.println("Snuke");
        }
    }
}