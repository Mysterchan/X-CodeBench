import java.util.*;

class Main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int N = ni();
        int[] P = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            P[i] = i;
        }
        int Q = ni();
        while (Q-- > 0) {
            int q = ni();
            if (q == 1) {
                int a = ni();
                int b = ni();
                P[a] = b;
            } else if (q == 2) {
                int a = ni();
                int b = ni();
                // Swap nests a and b
                for (int i = 1; i <= N; i++) {
                    if (P[i] == a) {
                        P[i] = b;
                    } else if (P[i] == b) {
                        P[i] = a;
                    }
                }
            } else if (q == 3) {
                int a = ni();
                System.out.println(P[a]);
            }
        }

        sc.close();
    }

    static int ni() {
        return sc.nextInt();
    }
}