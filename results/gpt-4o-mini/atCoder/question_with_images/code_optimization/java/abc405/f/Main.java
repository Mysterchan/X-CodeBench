import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        int[][] segments = new int[M][2];
        Map<Integer, List<Integer>> pointToSegment = new HashMap<>();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            segments[i][0] = a;
            segments[i][1] = b;
            pointToSegment.computeIfAbsent(a, x -> new ArrayList<>()).add(i);
            pointToSegment.computeIfAbsent(b, x -> new ArrayList<>()).add(i);
        }
        
        int Q = Integer.parseInt(br.readLine());
        for (int q = 0; q < Q; q++) {
            st = new StringTokenizer(br.readLine());
            int c = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            
            Set<Integer> intersectingSegments = new HashSet<>();
            for (int point : new int[]{c, d}) {
                if (pointToSegment.containsKey(point)) {
                    for (int segIndex : pointToSegment.get(point)) {
                        int a = segments[segIndex][0];
                        int b = segments[segIndex][1];
                        if (intersects(a, b, c, d, 2 * N)) {
                            intersectingSegments.add(segIndex);
                        }
                    }
                }
            }
            
            pw.println(intersectingSegments.size());
        }

        pw.flush();
        pw.close();
        br.close();
    }

    static boolean intersects(int a, int b, int c, int d, int maxPoint) {
        if (a > b) {
            int temp = a; a = b; b = temp;
        }
        if (c > d) {
            int temp = c; c = d; d = temp;
        }
        boolean cBetweenAB = isBetweenInCircle(a, b, c, maxPoint);
        boolean dBetweenAB = isBetweenInCircle(a, b, d, maxPoint);
        return cBetweenAB != dBetweenAB;
    }

    static boolean isBetweenInCircle(int a, int b, int x, int maxPoint) {
        return (a < b) ? (a < x && x < b) : (x > a || x < b);
    }
}