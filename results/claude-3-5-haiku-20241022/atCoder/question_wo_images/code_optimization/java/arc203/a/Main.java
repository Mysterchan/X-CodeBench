import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            long n = sc.nextLong();
            long m = sc.nextLong();
            
            long result;
            if (m == 1) {
                result = 1;
            } else if (m == 2) {
                result = 2;
            } else {
                // m > 2
                // Pattern: each recursive call subtracts 2 from m and adds n
                // Until we reach base case (1 or 2)
                long base = (m % 2 == 0) ? 2 : 1;
                long steps = (m - base) / 2;
                result = base + n * steps;
            }
            
            System.out.println(result);
        }
        sc.close();
    }
}