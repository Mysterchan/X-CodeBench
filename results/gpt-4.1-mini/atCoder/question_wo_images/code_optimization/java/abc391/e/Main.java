import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br;
    static BufferedWriter bw;
    static int N;
    static int[] p;
    static int[] a;
    static int[][][] dp;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());
        p = new int[N + 1];
        p[0] = 1;
        for (int i = 1; i <= N; i++) {
            p[i] = p[i - 1] * 3;
        }

        char[] t = br.readLine().toCharArray();
        a = new int[p[N] + 1];
        for (int i = 1; i <= p[N]; i++) {
            a[i] = t[i - 1] - '0';
        }

        // dp[pos][level][val] = minimal changes to make the substring starting at pos of length 3^level have majority val
        dp = new int[p[N] + 1][N + 1][2];

        // Initialize dp for level 0 (single elements)
        for (int i = 1; i <= p[N]; i++) {
            dp[i][0][a[i]] = 0;
            dp[i][0][a[i] ^ 1] = 1;
        }

        // Build dp bottom-up
        for (int level = 1; level <= N; level++) {
            int len = p[level];
            int subLen = p[level - 1];
            for (int start = 1; start <= p[N]; start += len) {
                // For each group of 3 sub-blocks
                // We want to find minimal changes to get majority 0 or 1 at this level
                // Majority means at least 2 out of 3 sub-blocks have that value

                // For each sub-block, we have dp for val=0 and val=1
                // We need to pick at least 2 sub-blocks with val = majority_val

                // Collect costs for sub-blocks
                int[] cost0 = new int[3];
                int[] cost1 = new int[3];
                for (int i = 0; i < 3; i++) {
                    int pos = start + i * subLen;
                    cost0[i] = dp[pos][level - 1][0];
                    cost1[i] = dp[pos][level - 1][1];
                }

                // For majority 0:
                // Need at least 2 sub-blocks with val=0
                // So pick minimal sum of costs with at least 2 zeros
                dp[start][level][0] = minCostMajority(cost0, cost1, 0);

                // For majority 1:
                // Need at least 2 sub-blocks with val=1
                dp[start][level][1] = minCostMajority(cost0, cost1, 1);
            }
        }

        // The final majority value after N operations
        int finalVal = majorityValue(1, p[N], N);

        // Output minimal changes to flip finalVal
        bw.write(dp[1][N][finalVal ^ 1] + "\n");
        bw.flush();
    }

    // Compute minimal cost to get majority val (0 or 1) from 3 sub-blocks
    // cost0[i] = cost to make sub-block i majority 0
    // cost1[i] = cost to make sub-block i majority 1
    // We must pick at least 2 sub-blocks with val = majority_val
    static int minCostMajority(int[] cost0, int[] cost1, int majority_val) {
        // We have 3 sub-blocks, each can be chosen as majority_val or not
        // We want minimal sum of costs with at least 2 sub-blocks chosen as majority_val

        // For each sub-block, cost to choose majority_val is cost_majority_val[i]
        // cost to choose opposite is cost_opposite[i]

        int[] costMajor = majority_val == 0 ? cost0 : cost1;
        int[] costOpp = majority_val == 0 ? cost1 : cost0;

        // We want to pick at least 2 sub-blocks with majority_val
        // So possible patterns:
        // Choose all 3 as majority_val
        int sumAllMajor = costMajor[0] + costMajor[1] + costMajor[2];
        // Choose exactly 2 as majority_val and 1 as opposite
        // Try all 3 possibilities for the opposite one
        int minTwoMajor = Integer.MAX_VALUE;
        for (int i = 0; i < 3; i++) {
            int sum = 0;
            for (int j = 0; j < 3; j++) {
                if (j == i) sum += costOpp[j];
                else sum += costMajor[j];
            }
            if (sum < minTwoMajor) minTwoMajor = sum;
        }

        return Math.min(sumAllMajor, minTwoMajor);
    }

    // Compute the final majority value after N operations (without changes)
    static int majorityValue(int l, int r, int n) {
        if (n == 0) {
            return a[l];
        }
        int subLen = p[n - 1];
        int countOne = 0;
        int countZero = 0;
        for (int i = l; i <= r; i += subLen) {
            int val = majorityValue(i, i + subLen - 1, n - 1);
            if (val == 1) countOne++;
            else countZero++;
        }
        return countOne >= countZero ? 1 : 0;
    }
}