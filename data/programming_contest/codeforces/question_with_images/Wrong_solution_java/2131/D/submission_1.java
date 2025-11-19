import java.io.*;
import java.sql.SQLOutput;
import java.util.*;

public class Main {

    static Scanner sc=new Scanner(System.in);
    static StreamTokenizer st=new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static PrintWriter pw=new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static List<List<Integer>>v=new ArrayList<>();
    static long[]ten_pow=new long[20];
    public static void main(String[] args) throws IOException{
        ten_pow[0]=1;
        for(int i=1;i<=17;i++){
            ten_pow[i]=ten_pow[i-1]*10;
        }
        st.nextToken();
        int t=(int)st.nval;
        while(t-->0){
            solve();
        }
        pw.close();
    }
    static int n,ans=0;
    static List<Integer>[]al=new ArrayList[(int)2e5+5];
    static int[]rd=new int[(int)2e5+5];
    public static void solve()throws IOException{
        st.nextToken();
        int n=(int)st.nval;
        int max=0,ge=0;
        ans=Integer.MAX_VALUE;
        Arrays.fill(rd,0,n+1,0);
        for(int i=1;i<=n;i++){
            al[i]=new ArrayList<>();
        }
        List<Integer>algen=new ArrayList<>();
        for(int i=1;i<n;i++){
            st.nextToken();
            int u=(int)st.nval;
            st.nextToken();
            int v=(int)st.nval;
            al[u].add(v);
            al[v].add(u);
            rd[u]++;
            if(rd[u]>max){
                max=rd[u];
            }
            rd[v]++;
            if(rd[v]>max){
                max=rd[v];
            }
        }
        if(n<=3){
            pw.println(0);
            return;
        }
        int sum=0;
        for(int i=1;i<=n;i++){
            if(rd[i]==max){
                algen.add(i);
            }
            if(rd[i]==1){
                sum++;
            }
        }
        int temp=0;
        for(int x:algen){
            temp=0;
            for(int t:al[x]){
                if(rd[t]==1)temp++;
            }
            ans=Math.min(ans,sum-temp);
        }

        pw.println(ans);
    }


    public static void init(){
        for(int i=1;i<=(int)2e5+5;i++){
            v.add(new ArrayList<>());
        }
        for(int i=2;i<=(int)2e5;i++){
            for(int j=i;j<=(int)2e5;j+=i){
                v.get(j).add(i);
            }
        }
    }

    static class Node implements Comparable<Node>{
        int x;long y;
        public Node(int x,long y){
            this.x=x;
            this.y=y;
        }
        public Node(){}
        public int compareTo(Node o){
            return Long.compare(this.y,o.y);
        }
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Node node = (Node) o;
            return x == node.x && y == node.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

    public static long pow(long base,long e,long mod){
        long res=1;
        while(e>0){
            if((e&1)==1){
                res=res*base%mod;
            }
            e/=2;
            base=base*base%mod;
        }
        return res%mod;
    }
}
