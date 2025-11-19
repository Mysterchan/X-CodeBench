import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            long n = sc.nextInt();
            long m = sc.nextInt();
            System.out.println(solve(n, m));
        }
        sc.close();
    }

    private static long solve (long n, long m) {
        if (m <= 2) return m;

        return solve(n, m - 2) + n;
    }
}