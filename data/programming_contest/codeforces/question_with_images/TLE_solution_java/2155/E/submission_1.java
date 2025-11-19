import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        PrintWriter out = new PrintWriter(System.out);
        int t = fs.nextInt();
        while(t-->0){
            int n = fs.nextInt();
            int m = fs.nextInt();
            int k = fs.nextInt();

            int[] col = new int[m+1];
            int maxC = 0;
            for(int i=0; i<k; i++){
                int r = fs.nextInt();
                int c = fs.nextInt();

                maxC = Math.max(c, maxC);
                col[c] ^= 1;
            }

            boolean player1 = false;
            if(n==1){
                player1 = (m>=2 && col[2]==1) ? true : false;
            } else {
                for(int i=2; i<=maxC; i++){
                    if(col[i] == 1){
                        player1 = true;
                        break;
                    }
                }
            }

            out.println(player1 ? "Mimo" : "Yuyu");
        }
        out.flush();
    }
    static class FastScanner {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer("");
        String next() {
            while (!st.hasMoreTokens())
                try {
                    st=new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
        int[] readArray(int n) {
            int[] a=new int[n];
            for (int i=0; i<n; i++) a[i]=nextInt();
            return a;
        }
        long nextLong() {
            return Long.parseLong(next());
        }
    }
}
