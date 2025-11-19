import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        long[] A = new long[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextLong();
        }

        sc.close();

        if (N == 2) {
            System.out.println("Yes");
            return;
        }

        boolean isGeometric = true;

        for (int i = 1; i < N - 1; i++) {

            long lhs = A[i] * A[i];

            long rhs = A[i-1] * A[i+1];

            if (lhs != rhs) {
                isGeometric = false;
                break;
            }
        }

        if (isGeometric) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}