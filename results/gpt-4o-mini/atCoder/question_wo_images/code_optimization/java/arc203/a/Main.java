import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        StringBuilder result = new StringBuilder();
        
        while (t-- > 0) {
            long n = sc.nextInt();
            long m = sc.nextInt();
            result.append(maxPerfectRecordPlayers(n, m)).append("\n");
        }
        System.out.print(result);
        sc.close();
    }

    private static long maxPerfectRecordPlayers(long n, long m) {
        if (m <= 2) return m; // If M is 1 or 2, max perfect player is M
        
        // Each pair of players can potentially be winners.
        // The maximum perfect scores is the number of players that can uniquely win in each team match
        return (n - 1) * m;
    }
}