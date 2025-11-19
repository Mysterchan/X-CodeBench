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

            // We only need to track parity of tokens in each column
            // XOR parity for each column
            int[] col = new int[m+1];
            int maxC = 0;
            for(int i=0; i<k; i++){
                fs.nextInt(); // row not needed
                int c = fs.nextInt();
                if(c > maxC) maxC = c;
                col[c] ^= 1;
            }

            // If n == 1, only column 2 matters for a move
            // Otherwise, any column >= 2 with odd parity means first player can move
            boolean player1 = false;
            if(n == 1){
                player1 = (m >= 2 && col[2] == 1);
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
    }
}