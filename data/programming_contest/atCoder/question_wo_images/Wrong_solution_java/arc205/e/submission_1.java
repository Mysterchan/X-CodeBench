import java.io.*;
import java.util.*;

public class Main {
    static final int MOD = 998244353;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] a = new int[n];
        for(int i=0;i<n;i++) a[i]=Integer.parseInt(st.nextToken());
        int lim = 1<<20;
        long[] f = new long[lim];
        Arrays.fill(f,1);
        for(int x:a) f[x]=f[x]*x%MOD;
        for(int b=0;b<20;b++){
            for(int m=0;m<lim;m++){
                if(((m>>b)&1)==1) f[m]=f[m]*f[m^(1<<b)]%MOD;
            }
        }
        StringBuilder sb=new StringBuilder();
        for(int x:a) sb.append(f[x]).append('\n');
        System.out.print(sb);
    }
}