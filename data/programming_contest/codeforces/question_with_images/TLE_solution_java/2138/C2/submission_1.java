import java.util.*;

public class Main {
    static List<List<Integer>> al;
    static int[] lvlCnt;
    static int h;

    static int f1(int i, int z, int o, int[] l) {
        if( i >= h || (z < l[i] && o < l[i])) return 0 ;
        if(z >= l[i] && o >= l[i]) return 1 + Math.max(f1(i+1, z-l[i], o, l) , f1(i+1, z,o-l[i], l)) ;
        if(z >= l[i]) return 1 + f1(i+1, z - l[i], o, l) ;

        return 1 + f1(i+1, z, o- l[i], l) ;
    }
    static int f(int u) {
        if(al.get(u).isEmpty()) return 1 ;
        int mn = Integer.MAX_VALUE ;
        for(int v : al.get(u)) mn = Math.min(mn, f(v)) ;
        return mn+1 ;
    }
    static void dfs(int u, int d) {
        lvlCnt[d]++;
        for (int v : al.get(u)) dfs(v, d + 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0) {
            int n = sc.nextInt(), k = sc.nextInt();
            al = new ArrayList<>();
            for (int i = 0; i <= n; i++) al.add(new ArrayList<>());
            for (int i = 2; i <= n; i++) {
                int p = sc.nextInt();
                al.get(p).add(i);
            }

            lvlCnt = new int[n + 1];
            h = 0;
            dfs(1, 0);

            h = f(1);
            int z = k, o = n - k, ans = 0;


            ans = f1(0, z, o , lvlCnt) ;
            System.out.println(ans);
        }
    }
}
