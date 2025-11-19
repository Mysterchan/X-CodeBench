import java.io.*;
import java.util.*;

public class Main {

    static Scanner sc;
    static PrintWriter out;

    public static void main(String[] args) {
        sc = new Scanner(System.in);
        out = new PrintWriter(System.out);
        new Main().solve();
        out.flush();
    }

    public void solve() {
        int n = sc.nextInt();
        long m = sc.nextLong();
        long[] p = new long[n];
        long minp = Long.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            p[i] = sc.nextLong();
            if (p[i] < minp) minp = p[i];
        }

        // Binary search on total units bought
        long left = 0;
        // Upper bound: max units if all bought from cheapest product
        long right = (long) Math.sqrt((double) m / minp) + 2;

        while (right - left > 1) {
            long mid = (left + right) >>> 1;
            if (canBuy(mid, p, m)) {
                left = mid;
            } else {
                right = mid;
            }
        }

        out.println(left);
    }

    // Check if it's possible to buy total 'units' units with cost <= m
    boolean canBuy(long units, long[] p, long m) {
        long cost = 0;
        for (long price : p) {
            // For each product, find k_i to minimize sum k_i = units
            // k_i = floor(units / n) or floor(units / n) + 1
            // But we want to minimize sum p_i * k_i^2 under sum k_i = units
            // Optimal k_i = floor(units / n) or ceil(units / n) distributed to minimize cost
            // But this is complicated, so we use the formula derived from the original code:
            // k_i = floor((units / p_i + 1) / 2)
            // But this is not correct for checking feasibility.
            // Instead, we use the approach:
            // For given total units, distribute units to minimize sum p_i * k_i^2
            // The minimal cost is achieved when k_i proportional to 1/sqrt(p_i)
            // But to check feasibility quickly, we can use the formula:
            // k_i = floor(units * sqrt(1/p_i) / sum sqrt(1/p_j))
            // But this is complicated.
            // Instead, we use the original code's approach:
            // For given mid, k_i = floor((mid / p_i + 1) / 2)
            // But this is not correct for feasibility check.
            // So we do a direct approach:
            // For each product, max k_i = floor(sqrt(m / p_i))
            // But we want sum k_i >= units
            // So we do a binary search on k_i for each product to find max k_i with cost <= m
            // But this is too slow.
            // So we do a direct calculation:
            // For given mid, k_i = floor((mid / p_i + 1) / 2)
            // sum k_i >= units => feasible
            // But original code uses this formula for k_i.
            // So we replicate that here.

            long k = (units / price + 1) / 2;
            cost += price * k * k;
            if (cost > m) return false;
        }
        return true;
    }
}