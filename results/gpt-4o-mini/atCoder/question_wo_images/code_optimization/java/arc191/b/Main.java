import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        StringBuilder result = new StringBuilder();
        
        while (t-- > 0) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            
            // To find at least K compatible integers
            int count = 0;
            int x = n; // Start checking from n
            
            while (count < k) {
                if ((x ^ n) == (x % n)) {
                    count++;
                    if (count == k) {
                        result.append(x).append("\n");
                        break;
                    }
                }
                x++;
            }
            
            if (count < k) {
                result.append("-1\n");
            }
        }
        System.out.print(result);
    }
}