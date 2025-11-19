import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        // Use a HashMap to count occurrences of edges between nodes
        Map<Integer, Map<Integer, Integer>> edgeCount = new HashMap<>();
        int result = 0;

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            
            if (u == v) {
                // Count self-loops
                result++;
            } else {
                // Ensure u is always less than v for consistency
                if (u > v) {
                    int temp = u;
                    u = v;
                    v = temp;
                }
                
                // Initialize the inner map if not present
                edgeCount.putIfAbsent(u, new HashMap<>());
                // Count the edges between u and v
                result += edgeCount.get(u).getOrDefault(v, 0);
                edgeCount.get(u).put(v, edgeCount.get(u).getOrDefault(v, 0) + 1);
            }
        }
        
        System.out.println(result);
    }
}