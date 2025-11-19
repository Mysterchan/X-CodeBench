import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class Main {

    static void solve(BufferedReader br, PrintWriter pw) throws Exception {
        String[] parts = br.readLine().trim().split(" ");
        int n = Integer.parseInt(parts[0]);
        int k = Integer.parseInt(parts[1]);

        int[] p = new int[n];
        p[0] = -1;
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        parts = br.readLine().trim().split(" ");
        for (int i = 0; i < n - 1; i++) {
            int x = Integer.parseInt(parts[i]) - 1;
            p[i + 1] = x;
            adj.get(x).add(i + 1);
        }

        ArrayList<Integer> s = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();
        q.add(0);
        boolean f = true;

        while (f) {
            int sz = q.size();
            int y = sz;
            while (y-- > 0) {
                int x = q.poll();
                if (adj.get(x).isEmpty()) {
                    f = false;
                }
                for (int i : adj.get(x)) {
                    q.add(i);
                }
            }
            s.add(sz);
        }

        int total = 0;
        for (int val : s) total += val;

        TreeSet<Integer> m = new TreeSet<>();
        m.add(k);

        for (int i = s.size() - 1; i >= 0; i--) {
            Integer it = m.ceiling(s.get(i));
            if (it == null) continue;
            m.add(it - s.get(i));
        }

        if (n - total >= m.first()) {
            pw.println(s.size());
        } else {
            pw.println(s.size() - 1);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        int t = Integer.parseInt(br.readLine().trim());
        while (t-- > 0) {
            solve(br, pw);
        }

        pw.flush();
    }
}
