import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] hw = br.readLine().split(" ");
        int H = Integer.parseInt(hw[0]);
        int W = Integer.parseInt(hw[1]);

        int[] rows = new int[H];
        for (int i = 0; i < H; i++) {
            String s = br.readLine();
            int rowBits = 0;
            for (int j = 0; j < W; j++) {
                if (s.charAt(j) == '1') {
                    rowBits |= (1 << j);
                }
            }
            rows[i] = rowBits;
        }

        int min = Integer.MAX_VALUE;
        int limit = 1 << W;

        // Precompute bit counts for all possible W-bit numbers
        int[] bitCount = new int[limit];
        for (int i = 0; i < limit; i++) {
            bitCount[i] = Integer.bitCount(i);
        }

        // For each possible column flip pattern (mask)
        for (int mask = 0; mask < limit; mask++) {
            int total = 0;
            for (int i = 0; i < H; i++) {
                // XOR row with mask to simulate column flips
                int flipped = rows[i] ^ mask;
                // Count number of 1s after flips
                int ones = bitCount[flipped];
                // For each row, we can flip the entire row or not, choose minimal
                total += Math.min(ones, W - ones);
            }
            if (total < min) {
                min = total;
            }
        }

        System.out.println(min);
    }
}