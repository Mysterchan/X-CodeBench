import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // Use a HashSet of long to store edges uniquely.
        // Encode edge as a long: (min_vertex * (long)1_000_000_000) + max_vertex
        // Since N <= 2*10^5, 1_000_000_000 is safe multiplier to avoid collisions.
        HashSet<Long> edges = new HashSet<>(m);
        int removeCount = 0;

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            if (u == v) {
                // Self-loop must be removed
                removeCount++;
            } else {
                int a = Math.min(u, v);
                int b = Math.max(u, v);
                long code = ((long) a) * 1_000_000_000L + b;
                if (!edges.add(code)) {
                    // Duplicate edge found
                    removeCount++;
                }
            }
        }
        System.out.println(removeCount);
    }
}