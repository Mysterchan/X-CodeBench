import java.util.*;
import java.io.*;
import java.math.*;
public class Main {
    static final int N=300010;
    static int[] x=new int[N];
    static int[] cnt=new int[N];
    static int[] y=new int[N];
    static int n, m, sum;
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out=new PrintWriter(new OutputStreamWriter(System.out));
        StringTokenizer st=new StringTokenizer(br.readLine());
        n=Integer.parseInt(st.nextToken());
        m=Integer.parseInt(st.nextToken());
        for(int i=1;i<=m;i++){
            st=new StringTokenizer(br.readLine());
            x[i]=Integer.parseInt(st.nextToken());
            y[i]=Integer.parseInt(st.nextToken());
            cnt[i]=x[i]+y[i];
            for(int j=1;j<i;j++){
                if(x[i]-x[j]==y[j]-y[i]||x[i]+n-x[j]==y[j]-y[i]||x[i]-x[j]==y[j]-y[i]+n) continue;
                sum++;
            }
        }
        out.println(sum);
        out.close();
    }
}