import java.util.Scanner;

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

            boolean res = canMatch(a, b);
            System.out.println(res ? "Yes" : "No");
        }
    }

    static boolean canMatch(int[] a, int[] b) {
        // Count the number of 1s and 0s in A and B
        int countA1 = 0, countA0 = 0, countB1 = 0, countB0 = 0;
        
        for (int i = 0; i < a.length; i++) {
            if (a[i] == 1) countA1++;
            else countA0++;
            
            if (b[i] == 1) countB1++;
            else countB0++;
        }

        // To match A and B:
        // - The number of 1s must be the same
        // - The number of 0s must be the same
        return countA1 == countB1 && countA0 == countB0;
    }
}