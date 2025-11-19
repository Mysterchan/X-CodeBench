import java.util.Scanner;
import java.util.Arrays;

public class Main {

    static String A;

    static long min4(long a, long b, long c, long d) {
        return Math.min(Math.min(a, b), Math.min(c, d));
    }

    static long[] solve(int level, int l, int r) {

        if (r - l == 1) {
            char c = A.charAt(l);
            if (c == '0') {
                return new long[]{0, 1};
            } else {
                return new long[]{1, 0};
            }
        }

        int len = (r - l) / 3;
        int m1 = l + len;
        int m2 = l + 2 * len;

        long[] c1 = solve(level + 1, l, m1);
        long[] c2 = solve(level + 1, m1, m2);
        long[] c3 = solve(level + 1, m2, r);

        long cost0 = min4(
            c1[0] + c2[0] + c3[0],
            c1[0] + c2[0] + c3[1],
            c1[0] + c2[1] + c3[0],
            c1[1] + c2[0] + c3[0]
        );

        long cost1 = min4(
            c1[1] + c2[1] + c3[1],
            c1[1] + c2[1] + c3[0],
            c1[1] + c2[0] + c3[1],
            c1[0] + c2[1] + c3[1]
        );

        return new long[]{cost0, cost1};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        A = sc.next();
        sc.close();

        long[] root_costs = solve(0, 0, A.length());

        if (root_costs[0] == 0) {

            System.out.println(root_costs[1]);
        } else {

            System.out.println(root_costs[0]);
        }
    }
}