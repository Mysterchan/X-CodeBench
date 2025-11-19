import java.io.*;
import java.util.*;

public class Main {
    static class Triple {
        int i, j, k;
        long val;

        public Triple(int i, int j, int k, long val) {
            this.i = i;
            this.j = j;
            this.k = k;
            this.val = val;
        }
    }

    public static void main(String[] args) throws IOException {
        FastReader fr = new FastReader();
        FastWriter fw = new FastWriter();

        int n = fr.nextInt();
        int K = fr.nextInt();

        long[] A = new long[n];
        long[] B = new long[n];
        long[] C = new long[n];

        for (int i = 0; i < n; i++) A[i] = fr.nextLong();
        for (int i = 0; i < n; i++) B[i] = fr.nextLong();
        for (int i = 0; i < n; i++) C[i] = fr.nextLong();

        Arrays.sort(A);
        Arrays.sort(B);
        Arrays.sort(C);

        // Precompute all A[i]*B[j] sums for top M pairs, where M = min(N*N, K)
        // We only need top K sums, so limit M to K or N*N whichever is smaller
        int M = Math.min(n * n, K);

        PriorityQueue<long[]> pqAB = new PriorityQueue<>((x, y) -> Long.compare(y[0], x[0]));
        // Each element: [sum, i, j]
        // Start from largest pair (n-1, n-1)
        pqAB.add(new long[]{A[n - 1] * B[n - 1], n - 1, n - 1});
        boolean[][] visitedAB = new boolean[n][n];
        visitedAB[n - 1][n - 1] = true;

        long[] AB = new long[M];
        int countAB = 0;

        while (countAB < M && !pqAB.isEmpty()) {
            long[] cur = pqAB.poll();
            long val = cur[0];
            int i = (int) cur[1];
            int j = (int) cur[2];
            AB[countAB++] = val;

            if (i - 1 >= 0 && !visitedAB[i - 1][j]) {
                visitedAB[i - 1][j] = true;
                pqAB.add(new long[]{A[i - 1] * B[j], i - 1, j});
            }
            if (j - 1 >= 0 && !visitedAB[i][j - 1]) {
                visitedAB[i][j - 1] = true;
                pqAB.add(new long[]{A[i] * B[j - 1], i, j - 1});
            }
        }

        // Now merge AB and C arrays to find top K sums of form AB[x] + B[j]*C[k] + C[k]*A[i]
        // But original formula is A_i*B_j + B_j*C_k + C_k*A_i
        // We can rewrite as (A_i*B_j) + (B_j*C_k) + (C_k*A_i)
        // But we have AB = A_i*B_j, so we need to add B_j*C_k + C_k*A_i
        // However, we don't know i and j from AB array alone, so we must store indices in AB array.

        // To fix this, we must store indices i,j in AB array, not just sums.

        // So redo AB computation storing sums and indices:

        // Recompute AB with indices stored
        // We'll store AB as array of objects with sum and indices

        class Pair {
            long val;
            int i, j;

            Pair(long val, int i, int j) {
                this.val = val;
                this.i = i;
                this.j = j;
            }
        }

        // Recompute AB with indices
        PriorityQueue<Pair> pqAB2 = new PriorityQueue<>((x, y) -> Long.compare(y.val, x.val));
        boolean[][] visitedAB2 = new boolean[n][n];
        pqAB2.add(new Pair(A[n - 1] * B[n - 1], n - 1, n - 1));
        visitedAB2[n - 1][n - 1] = true;

        Pair[] ABpairs = new Pair[M];
        int idxAB = 0;

        while (idxAB < M && !pqAB2.isEmpty()) {
            Pair cur = pqAB2.poll();
            ABpairs[idxAB++] = cur;

            int i = cur.i;
            int j = cur.j;

            if (i - 1 >= 0 && !visitedAB2[i - 1][j]) {
                visitedAB2[i - 1][j] = true;
                pqAB2.add(new Pair(A[i - 1] * B[j], i - 1, j));
            }
            if (j - 1 >= 0 && !visitedAB2[i][j - 1]) {
                visitedAB2[i][j - 1] = true;
                pqAB2.add(new Pair(A[i] * B[j - 1], i, j - 1));
            }
        }

        // Now we want to combine ABpairs with C to find top K sums of:
        // ABpairs[x].val + B[ABpairs[x].j]*C[k] + C[k]*A[ABpairs[x].i]
        // = ABpairs[x].val + C[k]*(B[j] + A[i])

        // So for each ABpair, define S = B[j] + A[i]
        // Then total sum = ABpairs[x].val + C[k]*S

        // We want top K sums over all x,k pairs:
        // sum = ABpairs[x].val + C[k]*S_x

        // We can think of this as merging two arrays:
        // ABpairs sorted descending by val
        // C sorted descending
        // For each ABpair, S_x = B[j] + A[i]

        // We want top K sums of ABpairs[x].val + C[k]*S_x

        // We can do a best-first search with a max-heap over pairs (x,k)

        // Precompute S array:
        long[] S = new long[M];
        for (int i = 0; i < M; i++) {
            S[i] = B[ABpairs[i].j] + A[ABpairs[i].i];
        }

        // Sort C descending
        Arrays.sort(C);
        for (int i = 0; i < n / 2; i++) {
            long temp = C[i];
            C[i] = C[n - 1 - i];
            C[n - 1 - i] = temp;
        }

        // Priority queue for pairs (x,k) with sum = ABpairs[x].val + C[k]*S[x]
        PriorityQueue<long[]> pq = new PriorityQueue<>((x, y) -> Long.compare(y[0], x[0]));
        // Each element: [sum, x, k]

        boolean[][] visited = new boolean[M][Math.min(n, K)]; // limit k dimension to min(n,K) to save memory

        int maxK = Math.min(n, K);

        pq.add(new long[]{ABpairs[0].val + C[0] * S[0], 0, 0});
        visited[0][0] = true;

        long answer = 0;
        int count = 0;

        while (count < K && !pq.isEmpty()) {
            long[] cur = pq.poll();
            long val = cur[0];
            int x = (int) cur[1];
            int k = (int) cur[2];
            answer = val;
            count++;

            if (x + 1 < M && !visited[x + 1][k]) {
                visited[x + 1][k] = true;
                pq.add(new long[]{ABpairs[x + 1].val + C[k] * S[x + 1], x + 1, k});
            }
            if (k + 1 < maxK && !visited[x][k + 1]) {
                visited[x][k + 1] = true;
                pq.add(new long[]{ABpairs[x].val + C[k + 1] * S[x], x, k + 1});
            }
        }

        fw.println(answer);
        fw.flush();
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    String line = br.readLine();
                    if (line == null) return null;
                    st = new StringTokenizer(line);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }

    static class FastWriter {
        BufferedWriter bw;

        public FastWriter() {
            bw = new BufferedWriter(new OutputStreamWriter(System.out));
        }

        void println(long x) throws IOException {
            bw.write(Long.toString(x));
            bw.newLine();
        }

        void flush() throws IOException {
            bw.flush();
        }
    }
}