import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] a = new long[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextLong();
        }
        
        if (n == 2) {
            System.out.println("Yes");
            return;
        }

        long ratio = a[1] * a[1]; // To avoid division, we use multiplication
        for (int i = 1; i < n; i++) {
            if (a[i] * a[i - 1] != ratio) {
                System.out.println("No");
                sc.close();
                return;
            }
            ratio = a[i] * a[i]; // Update the ratio for the next pair
        }
        
        System.out.println("Yes");
        sc.close();
    }
}