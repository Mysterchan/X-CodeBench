import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter pw = new PrintWriter(System.out);

        int T=Integer.parseInt(r.readLine());
        long m = 998244353;
        while(T-->0){
            int N= Integer.parseInt(r.readLine());
            int[] vals = new int[N];

            long[] fact = new long[N+4];
            long[] ifact = new long[N+4];
            fact[0]=1;
            ifact[0]=1;
            for(int i=1; i<N+4; i++)
            {
                fact[i]=(fact[i-1]*i)%m;
                ifact[i] = inverse(fact[i], m)%m;
            }


            StringTokenizer st = new StringTokenizer(r.readLine());
            for(int i=0; i<N; i++){
                vals[i]=Integer.parseInt(st.nextToken());
            }
            long ways =1;
            int spots=0;
            int sum=0;
            for(int i=N-1; i>=0; i--){
                sum+=vals[i];
                if(2*i<=N-2)
                    spots+=2;
                if(2*i==N-1)
                    spots++;
                if(vals[i]>spots)
                {
                    ways=0;
                    break;
                }
                else{
                    ways = (((ways*fact[spots])%m)*((ifact[spots-vals[i]]*ifact[vals[i]])%m))%m;
                    spots-=vals[i];
                }
            }
            if(sum==N)
                pw.println(ways);
            else
                pw.println(0);
        }
		pw.close();
	}

    public static long inverse(long b, long m){
        return pow(b, m-2, m);
    }

    public static long pow(long b, long p, long m){
        if(p==0)
            return 1;
        long res = pow((b*b)%m, p/2, m);
        if(p%2==0)
            return res;
        return (b*res)%m;
    }
}
