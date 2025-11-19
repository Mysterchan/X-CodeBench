import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int R = sc.nextInt();
        long R2 = (long) R * R;
        long count = 0;

        // We iterate over i from 1 to R
        // For each i, find max j >= 0 such that all four corners of the square centered at (i,j) are inside the circle.
        // The farthest corner from origin is (i+0.5, j+0.5), so check (i+0.5)^2 + (j+0.5)^2 <= R^2
        // For each i, find max j satisfying (i+0.5)^2 + (j+0.5)^2 <= R^2
        // j_max = floor( sqrt(R^2 - (i+0.5)^2) - 0.5 )

        for (int i = 1; i <= R; i++) {
            double x = i + 0.5;
            double val = R2 - x * x;
            if (val < 0) break; // no j possible for larger i
            int jMax = (int) Math.floor(Math.sqrt(val) - 0.5);
            if (jMax < 0) continue;
            count += jMax + 1; // j from 0 to jMax inclusive
        }

        // count squares in first quadrant excluding axes
        // multiply by 4 for all four quadrants
        // add 1 for the center square at (0,0)
        System.out.println(count * 4 + 1);
    }
}