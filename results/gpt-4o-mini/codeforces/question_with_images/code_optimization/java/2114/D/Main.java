import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        for (int tc = 0; tc < t; ++tc) {
            int n = sc.nextInt();
            long[] x = new long[n];
            long[] y = new long[n];
            for (int i = 0; i < n; ++i) {
                x[i] = sc.nextLong();
                y[i] = sc.nextLong();
            }

            System.out.println(solve(n, x, y));
        }

        sc.close();
    }

    static long solve(int n, long[] x, long[] y) {
        if (n == 1) {
            return 1;
        }

        long minX = Long.MAX_VALUE, maxX = Long.MIN_VALUE;
        long minY = Long.MAX_VALUE, maxY = Long.MIN_VALUE;

        for (int i = 0; i < n; ++i) {
            minX = Math.min(minX, x[i]);
            maxX = Math.max(maxX, x[i]);
            minY = Math.min(minY, y[i]);
            maxY = Math.max(maxY, y[i]);
        }

        long xSize = maxX - minX + 1;
        long ySize = maxY - minY + 1;

        long result = xSize * ySize;

        if (result == n - 1) {
            result += Math.min(xSize, ySize);
        }

        return result;
    }
}