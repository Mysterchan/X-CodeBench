import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] A = new int[N];

        for (int i = 0; i < N; i++) {
            A[i] = scanner.nextInt();
        }

        int count = 0;
        int j = 0;

        for (int i = 0; i < N; i++) {
            while (j < N && A[j] < 2 * A[i]) {
                j++;
            }
            count += N - j;
        }

        System.out.println(count);
    }
}