import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] x = new int[n];
        int[] y = new int[n];
        for (int i = 0; i < n; i++) {
            x[i] = sc.nextInt();
            y[i] = sc.nextInt();
        }
        
        Map<Integer, Map<Integer, Integer>> para = new HashMap<>();
        Map<Integer, Integer> mid = new HashMap<>();
        
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                int dx = x[i] - x[j];
                int dy = y[i] - y[j];

                // Count for the midpoints
                int midKey = x[i] + x[j];
                int midValue = y[i] + y[j];
                mid.put(midKey, mid.getOrDefault(midKey, 0) + 1); // count of midpoints
                
                if (dx == 0) {
                    dy = 1;
                } else if (dy == 0) {
                    dx = 1;
                }

                if (dx < 0) {
                    dx = -dx;
                    dy = -dy;
                }

                int g = gcd(Math.abs(dx), Math.abs(dy));
                dx /= g;
                dy /= g;

                para.putIfAbsent(dx, new HashMap<>());
                para.get(dx).put(dy, para.get(dx).getOrDefault(dy, 0) + 1);
            }
        }

        long ans = 0;
        // Calculate trapezoids from parallel lines
        for (Map<Integer, Integer> values : para.values()) {
            for (int count : values.values()) {
                if (count > 1) {
                    ans += (count * (count - 1L)) / 2; // choose 2 out of count
                }
            }
        }

        // Subtract the cases for midpoints that are the same when counting
        for (int count : mid.values()) {
            if (count > 1) {
                ans -= (count * (count - 1L)) / 2; // choose 2 out of count
            }
        }

        System.out.println(ans);
        sc.close();
    }

    static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}