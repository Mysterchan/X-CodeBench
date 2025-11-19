import java.util.*;

public class Main {
    static long L, R;
    static String sL, sR;
    static int lenL, lenR;

    // dp cache: pos, isPrefixL, isPrefixR, topDigit, hasStarted
    // Using Integer for topDigit: 0-9, -1 means not set yet
    static Long[][][][][] dp;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        L = sc.nextLong();
        R = sc.nextLong();
        sc.close();

        sL = Long.toString(L);
        sR = Long.toString(R);
        lenL = sL.length();
        lenR = sR.length();

        long result = 0;
        // Count snake numbers with length from lenL to lenR
        for (int length = lenL; length <= lenR; length++) {
            // Prepare dp cache for this length
            dp = new Long[length + 1][2][2][11][2];
            // For each length, define lower and upper bounds for that length
            // If length == lenL, lower bound is sL, else 10^(length-1)
            // If length == lenR, upper bound is sR, else 10^length - 1

            String lowBound = (length == lenL) ? sL : "1" + "0".repeat(length - 1);
            String highBound = (length == lenR) ? sR : "9".repeat(length);

            result += dfs(0, true, true, -1, false, lowBound, highBound);
        }

        System.out.println(result);
    }

    // pos: current digit index
    // isPrefixL: whether current prefix equals lowBound prefix
    // isPrefixR: whether current prefix equals highBound prefix
    // topDigit: the top digit chosen (0-9), -1 if not chosen yet
    // hasStarted: whether we have started placing digits (to avoid leading zeros)
    // lowBound, highBound: strings representing current bounds for this length
    static long dfs(int pos, boolean isPrefixL, boolean isPrefixR, int topDigit, boolean hasStarted, String lowBound, String highBound) {
        if (pos == lowBound.length()) {
            // If number started and topDigit chosen, count 1, else 0
            return (hasStarted && topDigit != -1) ? 1 : 0;
        }
        if (dp[pos][isPrefixL ? 1 : 0][isPrefixR ? 1 : 0][topDigit == -1 ? 10 : topDigit][hasStarted ? 1 : 0] != null)
            return dp[pos][isPrefixL ? 1 : 0][isPrefixR ? 1 : 0][topDigit == -1 ? 10 : topDigit][hasStarted ? 1 : 0];

        long res = 0;
        int lowDigit = lowBound.charAt(pos) - '0';
        int highDigit = highBound.charAt(pos) - '0';

        for (int d = lowDigit; d <= highDigit; d++) {
            boolean nextIsPrefixL = isPrefixL && (d == lowDigit);
            boolean nextIsPrefixR = isPrefixR && (d == highDigit);
            boolean nextHasStarted = hasStarted || (d != 0);

            if (!nextHasStarted) {
                // Still leading zeros, topDigit not chosen yet
                // We can continue with topDigit = -1
                res += dfs(pos + 1, nextIsPrefixL, nextIsPrefixR, -1, false, lowBound, highBound);
            } else {
                if (topDigit == -1) {
                    // Choose topDigit as d (must be >=1 because number started)
                    // topDigit must be >=1 because number >=10
                    // But leading zeros are skipped, so first non-zero digit is topDigit candidate
                    // topDigit must be >=1 (digits 1-9)
                    if (d == 0) continue; // topDigit can't be zero
                    res += dfs(pos + 1, nextIsPrefixL, nextIsPrefixR, d, true, lowBound, highBound);
                } else {
                    // topDigit chosen, check snake condition: topDigit > every other digit
                    // So current digit d must be < topDigit
                    if (d < topDigit) {
                        res += dfs(pos + 1, nextIsPrefixL, nextIsPrefixR, topDigit, true, lowBound, highBound);
                    }
                    // else skip this digit as it violates snake condition
                }
            }
        }

        dp[pos][isPrefixL ? 1 : 0][isPrefixR ? 1 : 0][topDigit == -1 ? 10 : topDigit][hasStarted ? 1 : 0] = res;
        return res;
    }
}