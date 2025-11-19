import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = scanner.nextInt();
        }

        boolean hasZero = false;
        for (int i = 0; i < N; i++) {
            if (A[i] == 0) {
                hasZero = true;
                break;
            }
        }

        if (!hasZero) {
            System.out.println("Yes");
            return;
        }

        int[] B = new int[N];
        for (int i = 0; i < N; i++) {
            B[i] = A[(i - 1 + N) % N] + A[i] + A[(i + 1) % N];
        }

        boolean possible = true;
        for (int i = 0; i < N; i++) {
            if (A[i] == 0 && B[i] < 2) {
                possible = false;
                break;
            }
        }

        if (possible) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}