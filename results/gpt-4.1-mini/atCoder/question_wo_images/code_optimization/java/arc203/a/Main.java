import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            long n = sc.nextLong();
            long m = sc.nextLong();

            long result;
            if (m <= 2) {
                result = m;
            } else {
                // The recurrence solve(n, m) = solve(n, m-2) + n
                // with base cases solve(n,1)=1, solve(n,2)=2
                // can be solved as:
                // For even m: result = m/2 * n
                // For odd m: result = ((m-1)/2)*n + 1
                if (m % 2 == 0) {
                    result = (m / 2) * n;
                } else {
                    result = ((m - 1) / 2) * n + 1;
                }
            }

            System.out.println(result);
        }
        sc.close();
    }
}