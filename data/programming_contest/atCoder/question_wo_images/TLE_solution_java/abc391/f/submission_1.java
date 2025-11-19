import java.io.*;
import java.util.*;

public class Main{
    static class Triple {
        int f, s, p;
        long cost;

        public Triple(int f, int s, int p, long cost) {
            this.f = f;
            this.s = s;
            this.p = p;
            this.cost = cost;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Triple triple = (Triple) obj;
            return f == triple.f && s == triple.s && p == triple.p;
        }

        @Override
        public int hashCode() {
            return Objects.hash(f, s, p);
        }
    }

    public static void main(String[] args) throws IOException {
        FastReader fr = new FastReader();
        FastWriter fw = new FastWriter();

        int n = fr.nextInt();
        int k = fr.nextInt();

        long[] a = new long[n];
        long[] b = new long[n];
        long[] c = new long[n];

        for (int i = 0; i < n; i++) a[i] = fr.nextLong();
        for (int i = 0; i < n; i++) b[i] = fr.nextLong();
        for (int i = 0; i < n; i++) c[i] = fr.nextLong();

        Arrays.sort(a);
        Arrays.sort(b);
        Arrays.sort(c);

        PriorityQueue<Triple> pq = new PriorityQueue<>((x, y) -> Long.compare(y.cost, x.cost));
        ArrayList<Long> ans = new ArrayList<>();
        HashMap<Triple, Integer> vis = new HashMap<>();

        long cost = a[n-1] * b[n-1] + b[n-1] * c[n-1] + c[n-1] * a[n-1];
        Triple start = new Triple(n-1, n-1, n-1, cost);
        pq.add(start);
        vis.put(start, 1);

        while (ans.size() < k && !pq.isEmpty()) {
            Triple it = pq.poll();
            int rp = it.f, cp = it.s, pp = it.p;
            ans.add(it.cost);

            insertIfValid(pq, vis, a, b, c, rp - 1, cp, pp);
            insertIfValid(pq, vis, a, b, c, rp, cp - 1, pp);
            insertIfValid(pq, vis, a, b, c, rp, cp, pp - 1);
        }

        fw.println(ans.get(k - 1));
        fw.flush();
    }

    private static void insertIfValid(PriorityQueue<Triple> pq, HashMap<Triple, Integer> vis, long[] a, long[] b, long[] c, int f, int s, int p) {
        if (f >= 0 && s >= 0 && p >= 0) {
            Triple key = new Triple(f, s, p, 0);
            if (!vis.containsKey(key)) {
                long newCost = a[f] * b[s] + b[s] * c[p] + c[p] * a[f];
                pq.add(new Triple(f, s, p, newCost));
                vis.put(key, 1);
            }
        }
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
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() { return Integer.parseInt(next()); }
        long nextLong() { return Long.parseLong(next()); }
        double nextDouble() { return Double.parseDouble(next()); }
        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }

    static class FastWriter {
        BufferedWriter bw;

        public FastWriter() {
            bw = new BufferedWriter(new OutputStreamWriter(System.out));
        }

        void print(String s) throws IOException { bw.write(s); }
        void println(String s) throws IOException { bw.write(s + "\n"); }
        void println(long x) throws IOException { bw.write(x + "\n"); }
        void flush() throws IOException { bw.flush(); }
        void close() throws IOException { bw.close(); }
    }
}