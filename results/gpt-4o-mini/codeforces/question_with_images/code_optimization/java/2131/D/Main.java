import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        
        while (T-- > 0) {
            int n = scanner.nextInt();
            if (n <= 3) {
                System.out.println(0);
                continue;
            }
            
            int[] degree = new int[n + 1];
            for (int i = 0; i < n - 1; i++) {
                int u = scanner.nextInt();
                int v = scanner.nextInt();
                degree[u]++;
                degree[v]++;
            }
            
            int leafCount = 0;
            int maxLeafConnections = 0;
            
            for (int i = 1; i <= n; i++) {
                if (degree[i] == 1) {
                    leafCount++;
                } else {
                    maxLeafConnections = Math.max(maxLeafConnections, degree[i]);
                }
            }
            
            System.out.println(leafCount - maxLeafConnections);
        }
    }
}