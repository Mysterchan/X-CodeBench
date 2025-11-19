import java.io.*;
import java.util.*;

public class Main {
    static final int MOD = 998244353;
    static class DSU {
        int[] p, sz;
        DSU(int n) {
            p = new int[n+2];
            sz = new int[n+2];
            for(int i=1; i<=n; i++) {
                p[i] = i;
                sz[i] = 1;
            }
        }
        int find(int x) {
            return p[x] == x?x : (p[x]=find(p[x]));
        }
        void unite(int a, int b) {
            a = find(a); b = find(b);
            if(a==b) return;
            if(sz[a]>sz[b]) {
                int t = a; a = b; b = t;
            }
            p[a] = b;
            sz[b] += sz[a];
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedOutputStream(System.out));
        int t = Integer.parseInt(br.readLine().trim());
        while(t-->0) {
            int n = Integer.parseInt(br.readLine().trim());
            int[] p = new int[n+1], pos = new int[n+1];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int i=1; i<=n; i++) {
                p[i] = Integer.parseInt(st.nextToken());
                pos[p[i]] = i;
            }
            int[] c = new int[n+2];
            st = new StringTokenizer(br.readLine());
            for(int i=1; i<=n; i++) c[i] = Integer.parseInt(st.nextToken());
            int[] L = new int[n+2], R = new int[n+2];
            for(int i=0; i<=n+1; i++) {
                L[i] = i-1;
                R[i] = i+1;
            }
            DSU dsu = new DSU(n);
            for(int i=2; i<=n; i++) {
                if(c[i]==c[i-1]) {
                    dsu.unite(i, i-1);
                }
            }
            long ans = 1;
            for(int h=1; h<=n; h++) {
                int row = pos[h];
                int root = dsu.find(row);
                int ways = dsu.sz[root];
                ans = ans * ways % MOD;
                int l = L[row], r = R[row];
                R[l] = r;
                L[r] = l;
                dsu.sz[root]--;
                if(dsu.sz[root]==0
                    && l>=1 && r<=n
                    && c[l]==c[r]) {
                    dsu.unite(l, r);
                }
            }
            pw.println(ans);
        }
        pw.flush();
    }
}
