import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int[] A = new int[n];
            int[] B = new int[n];
            long a0 = 0;
            long b0 = 0;
            for (int i = 0; i < n; i++) {
                A[i] = sc.nextInt();
                a0 += A[i] == 1 ? 1 : 0;
            }

            for (int i = 0; i < n; i++) {
                B[i] = sc.nextInt();
                b0 += B[i] == 1 ? 1 : 0;
            }
            if (a0 != b0) {
                System.out.println("No");
            } else if ((a0 >= 2) || (a0 == 0) || (A[0] == B[0] && A[n - 1] == B[n - 1])) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }

        }
    }
}