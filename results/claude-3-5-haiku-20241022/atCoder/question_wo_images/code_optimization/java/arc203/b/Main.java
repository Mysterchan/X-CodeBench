import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int t = 0; t < T; t++) {
            int n = sc.nextInt();
            int[] a = new int[n];
            int[] b = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();
            for (int i = 0; i < n; i++) b[i] = sc.nextInt();

            System.out.println(solve(a, b) ? "Yes" : "No");
        }
    }

    static boolean solve(int[] a, int[] b) {
        int n = a.length;
        
        // Check if arrays are already equal
        boolean equal = true;
        for (int i = 0; i < n; i++) {
            if (a[i] != b[i]) {
                equal = false;
                break;
            }
        }
        if (equal) return true;
        
        // Count 1s in both arrays
        int sumA = 0, sumB = 0;
        for (int i = 0; i < n; i++) {
            sumA += a[i];
            sumB += b[i];
        }
        
        // If sums don't match, impossible
        if (sumA != sumB) return false;
        
        // If all elements are the same (all 0s or all 1s), 
        // we already checked equality above
        if (sumA == 0 || sumA == n) return false;
        
        // If we have both 0s and 1s, and sums match, we can reach any permutation
        // This is because:
        // - We can swap single 1s (choosing segments with sum=1)
        // - We can swap single 0s (choosing segments with sum=0)
        // - These operations allow arbitrary permutations
        return true;
    }
}