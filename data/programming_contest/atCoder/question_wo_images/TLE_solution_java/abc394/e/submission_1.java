import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        st.nextToken();
        int n = (int) st.nval;
        char[][] matrix = new char[n][n];
        st.ordinaryChar('-');
        st.wordChars('-', '-');
        for (int i = 0; i < n; i++) {
            st.nextToken();
            matrix[i] = st.sval.toCharArray();
        }

        HashMap<Short, LinkedList<Pair>> g = new HashMap<>(5*n*n+1);

        g.put((short) -1, new LinkedList<>());
        for (int i = 0; i < n; i++) {
            g.get((short)-1).add(new Pair(i*(n+1), 0));
        }
        HashMap<Character, LinkedList<Integer>> edge = new HashMap<>(5*n*n+1);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '-') continue;
                if (edge.containsKey(matrix[i][j])) {
                    for (Integer k : edge.get(matrix[i][j])) {
                        int a = k/n, b = k%n;

                        g.computeIfAbsent((short) (j*n+a), k_ -> new LinkedList<>())
                                .addFirst(new Pair(i*n+b, 2));
                        g.computeIfAbsent((short) (b*n+i), k_ -> new LinkedList<>())
                                .addFirst(new Pair(a*n+j, 2));
                    }
                }
                edge.computeIfAbsent(matrix[i][j], k -> new LinkedList<>()).add(i*n+j);
                if (i==j) continue;
                g.get((short)-1).add(new Pair(n*i+j, 1));
            }
        }
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(-1, 0));
        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], Integer.MAX_VALUE);
        }
        boolean[] visited = new boolean[n*n];
        Arrays.fill(visited, false);
        while (!q.isEmpty()) {
            Pair pair = q.poll();
            if (g.containsKey((short)pair.key)){
                for (Pair p : g.get((short)pair.key)){
                    if (visited[p.key]) continue;
                    int d = Math.min(dist[p.key/n][p.key%n], pair.val+p.val);
                    dist[p.key/n][p.key%n] = d;
                    q.add(new Pair(p.key, d));
                    visited[p.key] = true;
                }
            }
        }

        PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][j] == Integer.MAX_VALUE) {
                   out.print(-1 + " ");
                } else {
                    out.print(dist[i][j]+ " ");
                }
            }
            out.println();
        }
        out.flush();
    }

    private static class Pair{
        int key;
        int val;
        Pair(int key, int val){
            this.key = key;
            this.val = val;
        }
    }
}