import java.util.*;
import java.io.*;

public class Main {
    static final int N = 300010;
    static int[] x = new int[N];
    static int[] y = new int[N];
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= m; i++) {
            st = new StringTokenizer(br.readLine());
            x[i] = Integer.parseInt(st.nextToken());
            y[i] = Integer.parseInt(st.nextToken());
        }

        int intersectCount = 0;
        
        // Create a list that holds the endpoints of each line
        List<Pair> lines = new ArrayList<>();
        for (int i = 1; i <= m; i++) {
            lines.add(new Pair(x[i], y[i]));
        }

        // Sort lines based on their starting points (and end points in case of ties)
        lines.sort(Comparator.comparingInt((Pair p) -> p.start).thenComparingInt(p -> p.end));

        // Use a map to store the count of right endpoints we've seen 
        Map<Integer, Integer> endpointCount = new HashMap<>();

        for (Pair line : lines) {
            int start = line.start;
            int end = line.end;

            // Count intersecting lines
            for (int r : endpointCount.keySet()) {
                int cnt = endpointCount.get(r);
                // Check condition for intersection
                if (isIntersecting(start, end, r)) {
                    intersectCount += cnt;
                }
            }

            // Increment the count of the current right endpoint
            endpointCount.put(end, endpointCount.getOrDefault(end, 0) + 1);
        }

        out.println(intersectCount);
        out.close();
    }

    // Determines if the lines defined by (start, end) and (r, already counted end) intersect
    private static boolean isIntersecting(int start1, int end1, int r) {
        return (start1 < r && r < end1);
    }

    // Simple Pair class to hold pairs of endpoints
    static class Pair {
        int start, end;

        Pair(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
}