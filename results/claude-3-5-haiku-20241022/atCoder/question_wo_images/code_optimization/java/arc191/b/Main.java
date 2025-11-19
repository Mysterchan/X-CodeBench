import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while (t-- > 0) {
            long n = sc.nextLong();
            long k = sc.nextLong();
            
            // Find all bit positions where n has 0
            List<Integer> zeroBits = new ArrayList<>();
            for (int i = 0; i < 60; i++) {
                if ((n & (1L << i)) == 0) {
                    zeroBits.add(i);
                }
            }
            
            // Maximum compatible numbers = 2^(number of zero bits)
            if (k > (1L << zeroBits.size())) {
                System.out.println(-1);
                continue;
            }
            
            // Build the k-th compatible number
            // Start with n (ensures X >= n)
            long result = n;
            k--; // Convert to 0-indexed
            
            // Set bits according to k's binary representation
            for (int i = 0; i < zeroBits.size(); i++) {
                if ((k & (1L << i)) != 0) {
                    result |= (1L << zeroBits.get(i));
                }
            }
            
            System.out.println(result);
        }
        
        sc.close();
    }
}