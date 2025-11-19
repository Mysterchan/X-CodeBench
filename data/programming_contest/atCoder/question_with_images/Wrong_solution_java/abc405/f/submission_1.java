import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Read sc=new Read();
        int n=sc.nextInt();
        int m=sc.nextInt();
        List<Node2> nodes=new ArrayList<>();
        for(int i=0;i<m;i++){
            nodes.add(new Node2(sc.nextInt(),sc.nextInt()));
        }
        int q=sc.nextInt();
        while(q-->0){
            int ans=0;
            int a=sc.nextInt();
            for(int i=0;i<nodes.size();i++){
                if(nodes.get(i).l<=a&&nodes.get(i).r>=a)ans++;
            }
            int a2=sc.nextInt();
            for(int i=0;i<nodes.size();i++){
                if(nodes.get(i).l<=a2&&nodes.get(i).r>=a2)ans++;
            }
            System.out.println(ans);
        }
    }
}
class Node2{
    int l;
    int r;
    public Node2(int l,int r){
        this.l=l;
        this.r=r;
    }
}
class Read {
    BufferedReader bfr = new BufferedReader(new InputStreamReader(System.in));
    StreamTokenizer st = new StreamTokenizer(bfr);

    public int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }

    public long nextLong() throws IOException {
        st.nextToken();
        return (long) st.nval;
    }

    public Double nextDouble() throws IOException {
        st.nextToken();
        return (Double) st.nval;
    }

    public String nextLine() throws IOException {
        return bfr.readLine();
    }

    public String next() throws IOException {
        return st.sval;
    }
}