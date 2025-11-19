import java.util.*;
import java.io.*;

public class Main {
    static final int MOD = 998244353;
    static final int MAX = 200005;
    static long[] pow2 = new long[MAX];

    static void precomputePowers() {
        pow2[0] = 1;
        for (int i = 1; i < MAX; i++) {
            pow2[i] = (pow2[i - 1] * 2) % MOD;
        }
    }

    public static void main(String[] args) throws IOException {
        precomputePowers();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] hw = br.readLine().split(" ");
        int H = Integer.parseInt(hw[0]);
        int W = Integer.parseInt(hw[1]);

        long total = 0;

        long totalMatrices = (pow2[H] * pow2[W]) % MOD;

        for (int i = 1; i <= H; i++) {
            long rowPart = pow2[H - 1];
            long rowZero = pow2[W];
            long rowPrefix = pow2[W - 1];

            for (int j = 1; j <= W; j++) {

                long bad1 = (pow2[H - 1] * pow2[j - 1]) % MOD;
                long bad2 = (pow2[W - 1] * pow2[i - 1]) % MOD;
                long overlap = (pow2[H - 1] * pow2[W - 1]) % MOD;

                long bad = (bad1 + bad2 - overlap + MOD) % MOD;
                long good = (totalMatrices - bad + MOD) % MOD;

                total = (total + good) % MOD;
            }
        }

        System.out.println(total);
    }
}