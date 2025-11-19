import java.util.Scanner;
import java.math.BigInteger;

public class Main {

    static long N;
    static long M;
    static long[] P;

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
        BigInteger bigM = BigInteger.valueOf(M);

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
        N = sc.nextLong();
        M = sc.nextLong();
        P = new long[(int)N];
        for (int i = 0; i < N; i++) {
            P[i] = sc.nextLong();
        }

        long low = 0;

        long high = 3_000_000_000_000_000_000L;
        if (high < M) high = M * 3;

        long ansUnits = 0;
        BigInteger bigM = BigInteger.valueOf(M);

        while (low <= high) {
            long mid_T = low + (high - low) / 2;

            CheckResult result = check(mid_T);

            if (result.cost.compareTo(bigM) <= 0) {

                ansUnits = result.units;
                low = mid_T + 1;
            } else {

                high = mid_T - 1;
            }
        }

        System.out.println(ansUnits);
        sc.close();
    }
}