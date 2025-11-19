import java.util.*;

public class Main {

    static int H, W;
    static long[][] list;
    static long max = 0;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        H = scanner.nextInt();
        W = scanner.nextInt();
        list = new long[H][W];
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                list[i][j] = scanner.nextLong();
            }
        }
        findMaxScore();
        System.out.println(max);
    }

    static void findMaxScore() {
        int N = H * W;
        for (int mask = 0; mask < (1 << N); mask++) {
            if (isValidPlacement(mask)) {
                long currentScore = calculateXor(mask);
                max = Math.max(max, currentScore);
            }
        }
    }

    static boolean isValidPlacement(int mask) {
        boolean[][] covered = new boolean[H][W];
        for (int j = 0; j < N; j++) {
            if ((mask & (1 << j)) == 0) {
                int i = j / W;
                int k = j % W;

                if (covered[i][k]) return false; // Already covered

                // Check to place horizontally
                if (k + 1 < W && (mask & (1 << (j + 1))) == 0 && !covered[i][k + 1]) {
                    covered[i][k] = true;
                    covered[i][k + 1] = true;
                } 
                // Check to place vertically
                else if (i + 1 < H && (mask & (1 << (j + W))) == 0 && !covered[i + 1][k]) {
                    covered[i][k] = true;
                    covered[i + 1][k] = true;
                } 
                // Cannot place domino
                else {
                    return false;
                }
            }
        }
        return true;
    }

    static long calculateXor(int mask) {
        long xorValue = 0;
        for (int j = 0; j < (H * W); j++) {
            if ((mask & (1 << j)) == 0) {
                int i = j / W;
                int k = j % W;
                xorValue ^= list[i][k];
            }
        }
        return xorValue;
    }
}