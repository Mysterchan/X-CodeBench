import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        
        int[] b = new int[m];
        for (int i = 0; i < m; i++) {
            b[i] = sc.nextInt();
        }
        sc.close();
        
        // Find the leftmost subsequence matching B
        int[] minPos = new int[m];
        int aIdx = 0;
        for (int bIdx = 0; bIdx < m; bIdx++) {
            while (aIdx < n && a[aIdx] != b[bIdx]) {
                aIdx++;
            }
            if (aIdx >= n) {
                System.out.println("No");
                return;
            }
            minPos[bIdx] = aIdx;
            aIdx++;
        }
        
        // Find the rightmost subsequence matching B
        int[] maxPos = new int[m];
        aIdx = n - 1;
        for (int bIdx = m - 1; bIdx >= 0; bIdx--) {
            while (aIdx >= 0 && a[aIdx] != b[bIdx]) {
                aIdx--;
            }
            if (aIdx < 0) {
                System.out.println("No");
                return;
            }
            maxPos[bIdx] = aIdx;
            aIdx--;
        }
        
        // Check if there's flexibility (at least one position differs)
        for (int i = 0; i < m; i++) {
            if (minPos[i] != maxPos[i]) {
                System.out.println("Yes");
                return;
            }
        }
        
        System.out.println("No");
    }
}