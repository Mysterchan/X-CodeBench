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
        for (int i = 0; i < n; i++) {
            p[i] = sc.nextLong();
        }

        long totalUnits = 0;
        long left = 0, right = (long) Math.sqrt(2 * m) + 1;

        while (left < right) {
            long mid = (left + right + 1) / 2;
            long cost = 0;
            for (int i = 0; i < n; i++) {
                long k = mid / p[i];
                cost += k * k * p[i];
                if (cost > m) break; // Early exit if cost exceeds m
            }
            if (cost <= m) {
                totalUnits = mid; // mid is a valid total units
                left = mid; // Try for more units
            } else {
                right = mid - 1; // Try fewer units
            }
        }

        long remainingMoney = m;
        long totalPurchased = 0;

        for (int i = 0; i < n; i++) {
            long k = totalUnits / p[i];
            totalPurchased += k;
            remainingMoney -= k * k * p[i];
        }

        for (int i = 0; i < n; i++) {
            long k = totalUnits / p[i];
            long cost = p[i];
            while (remainingMoney >= cost) {
                remainingMoney -= cost;
                totalPurchased++;
                k++;
                cost = k * k * p[i] - (k - 1) * (k - 1) * p[i]; // Incremental cost
            }
        }

        out.println(totalPurchased);
    }
}