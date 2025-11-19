import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        FastScanner sc = new FastScanner();
        int N = sc.nextInt();
        
        int[] P = new int[N];
        for (int i = 0; i < N; i++) {
            P[i] = sc.nextInt();
        }
        
        int[] ans = new int[N];
        FenwickTree ft = new FenwickTree(N);
        
        for (int i = N - 1; i >= 0; i--) {
            int pos = ft.findKth(P[i]);
            ans[pos] = i + 1;
            ft.update(pos, 1);
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(ans[i]);
            if (i < N - 1) sb.append(" ");
        }
        System.out.println(sb);
    }
    
    static class FenwickTree {
        int[] tree;
        int n;
        
        FenwickTree(int n) {
            this.n = n;
            tree = new int[n + 1];
        }
        
        void update(int idx, int delta) {
            idx++;
            while (idx <= n) {
                tree[idx] += delta;
                idx += idx & -idx;
            }
        }
        
        int query(int idx) {
            idx++;
            int sum = 0;
            while (idx > 0) {
                sum += tree[idx];
                idx -= idx & -idx;
            }
            return sum;
        }
        
        int findKth(int k) {
            int left = 0, right = n - 1;
            while (left < right) {
                int mid = (left + right) / 2;
                int occupied = query(mid);
                int available = mid + 1 - occupied;
                if (available >= k) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }
            return left;
        }
    }

    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner() {
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

        int nextInt() {
            return Integer.parseInt(next());
        }
    }
}