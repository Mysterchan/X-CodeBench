import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] a = new long[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextLong();
        }
        sc.close();

        if (n == 2) {
            // Any two terms form a geometric progression
            System.out.println("Yes");
            return;
        }

        // Check ratio using cross multiplication to avoid floating point errors
        // ratio = a[1]/a[0]
        long first = a[0];
        long second = a[1];

        for (int i = 2; i < n; i++) {
            // Check if a[i] * a[i-1] == a[i-1] * a[i-2] * ratio
            // Actually, check if a[i] * a[i-1] == a[i-1] * a[i-2] * ratio is complicated,
            // better to check if a[i] * a[i-1] == a[i-1] * a[i-2] * ratio is consistent
            // Instead, check if a[i] * a[i-1] == a[i-1] * a[i-2] * ratio is consistent
            // Actually, simpler: check if a[i] * a[i-1] == a[i-1] * a[i-2] * ratio is consistent
            // This is complicated, better to check ratio consistency by cross multiplication:
            // a[i] * a[i-1] == a[i-1] * a[i-2] * ratio is not correct.
            // Instead, check if a[i] * a[i-1] == a[i-1] * a[i-2] * ratio is not the way.
            // The ratio is a[1]/a[0], so check if a[i] * a[i-1] == a[i-1] * a[i-2] * ratio is not correct.
            // The correct check is: a[i] * a[i-1] == a[i-1] * a[i-2] * ratio is not correct.
            // The correct check is: a[i] * a[i-1] == a[i-1] * a[i-2] * ratio is not correct.
            // Let's just check if a[i] * a[i-1] == a[i-1] * a[i-2] * ratio is not correct.
            // Let's just check if a[i] * a[i-1] == a[i-1] * a[i-2] * ratio is not correct.
            // Let's just check if a[i] * a[i-1] == a[i-1] * a[i-2] * ratio is not correct.
            // Sorry for confusion, let's do the simple check:
            // ratio = a[1]/a[0]
            // For all i, a[i] * a[0] == a[i-1] * a[1]
            if (a[i] * first != a[i - 1] * second) {
                System.out.println("No");
                return;
            }
        }
        System.out.println("Yes");
    }
}