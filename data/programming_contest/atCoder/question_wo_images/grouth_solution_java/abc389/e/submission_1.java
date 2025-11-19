import java.util.Scanner;
import java.math.BigInteger;

public class Main {

    static int N;
    static long M;
    static long[] P;
    static BigInteger bigM;

    static class CheckResult {
        BigInteger cost;
        long units;

        CheckResult(BigInteger cost, long units) {
            this.cost = cost;
            this.units = units;
        }
    }

    static CheckResult check(long T) {
        BigInteger totalCost = BigInteger.ZERO;
        long totalUnits = 0;

        for (int i = 0; i < N; i++) {
            if (P[i] == 0) continue;

            long k = (T / P[i] + 1) / 2;

            if (k == 0) continue;

            BigInteger bigK = BigInteger.valueOf(k);
            BigInteger bigP = BigInteger.valueOf(P[i]);

            BigInteger cost_i = bigK.multiply(bigK).multiply(bigP);

            totalCost = totalCost.add(cost_i);
            totalUnits += k;

            if (totalCost.compareTo(bigM) > 0) {
                return new CheckResult(totalCost, totalUnits);
            }
        }
        return new CheckResult(totalCost, totalUnits);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextLong();
        P = new long[N];
        for (int i = 0; i < N; i++) {
            P[i] = sc.nextLong();
        }

        bigM = BigInteger.valueOf(M);

        long low = 0;

        long high = 4_000_000_000_000_000_000L;

        long ansUnits = 0;
        BigInteger ansCost = BigInteger.ZERO;
        long best_T = -1;

        while (low <= high) {
            long mid_T = low + (high - low) / 2;
            if (mid_T < 0) {
                 high = mid_T - 1;
                 continue;
            }

            CheckResult result = check(mid_T);

            if (result.cost.compareTo(bigM) <= 0) {

                ansUnits = result.units;
                ansCost = result.cost;
                best_T = mid_T;
                low = mid_T + 1;
            } else {

                high = mid_T - 1;
            }
        }

        long M_rem_long = M - ansCost.longValue();
        if (M_rem_long < 0) M_rem_long = 0;

        long min_next_cost = Long.MAX_VALUE;
        long[] k_base = new long[N];
        long[] next_marginal_cost = new long[N];

        for (int i = 0; i < N; i++) {
            k_base[i] = ( (best_T / P[i]) + 1 ) / 2;

            next_marginal_cost[i] = (2 * k_base[i] + 1) * P[i];
            min_next_cost = Math.min(min_next_cost, next_marginal_cost[i]);
        }

        long items_at_min_cost = 0;
        for (int i = 0; i < N; i++) {
            if (next_marginal_cost[i] == min_next_cost) {
                items_at_min_cost++;
            }
        }

        long items_to_add = 0;
        if (min_next_cost > 0 && min_next_cost != Long.MAX_VALUE) {
            long items_we_can_afford = M_rem_long / min_next_cost;
            items_to_add = Math.min(items_we_can_afford, items_at_min_cost);
        }

        System.out.println(ansUnits + items_to_add);
        sc.close();
    }
}