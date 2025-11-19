import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            long s = sc.nextLong();
            int k = sc.nextInt();
            int ans = 0;

            for (int i = 0; i <= k; i++) {
                long totalDistance = i * (i + 1) / 2; // Distance Gleb can cover moving forward i turns
                if (totalDistance > s) {
                    break; // If the total distance goes beyond s, stop
                }
                ans = Math.max(ans, k - i); // Calculate remaining power
            }

            System.out.println(ans);
        }
        sc.close();
    }
}