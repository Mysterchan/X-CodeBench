import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int MAX = 500000;
        int[] diff = new int[MAX + 2]; // difference array for increments

        for (int i = 0; i < n; i++) {
            int L = s.nextInt();
            int R = s.nextInt();
            diff[L] += 1;
            if (R + 1 <= MAX) diff[R + 1] -= 1;
        }

        // Build prefix sums to get increments for each rating
        for (int i = 1; i <= MAX; i++) {
            diff[i] += diff[i - 1];
        }

        // Build prefix sums of increments to answer queries efficiently
        for (int i = 1; i <= MAX; i++) {
            diff[i] += diff[i - 1];
        }

        int q = s.nextInt();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < q; i++) {
            int x = s.nextInt();
            // final rating = initial rating + total increments for ratings <= x
            // increments for rating x is diff[x] - diff[x-1], but we want sum increments for all contests starting from x
            // Actually, the problem states increments happen if rating is in [L_i, R_i], and rating increases by 1 each time.
            // The increments are cumulative and depend on the rating after each contest.
            // But the problem is equivalent to: final rating = x + number of intervals that cover the rating or any rating after increments.
            // The original code uses a segment tree to map rating to final rating.
            // Our approach: since increments are +1 for each interval covering the rating, and rating increases by 1 each time,
            // the final rating after all contests is x + number of intervals covering the rating or any rating after increments.
            // But since increments are cumulative and rating increases by 1 each time, the final rating is x + number of intervals covering the rating or any rating after increments.
            // The difference array and prefix sums give us the total increments for each rating.
            // So final rating = x + diff[x]
            sb.append(x + diff[x]).append('\n');
        }
        System.out.print(sb);
    }
}