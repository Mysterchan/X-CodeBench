import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {

        static PrintWriter out = new PrintWriter(System.out);
        static FastReader in = new FastReader();

        public static void main(String[] args) {
            int t = 1;
            while (t-- > 0) {
                solve();
            }
            out.flush();
            out.close();
        }

        public static void solve() {
            int n=in.nextInt();
            long [] m=new long[n];
            for (int i=0;i<n;i++) {
                m[i] = in.nextInt();
            }
            int j=0;
            int ans=0;
            for (int i=0;i<n;i++){
                while (j<n&&m[i]*2>m[j]){
                    j++;
                }
                ans+=n-j;
            }
            out.println(ans);

        }

        static class FastReader {
            StringTokenizer st;
            BufferedReader br;

            public FastReader() {
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

            long nextLong() {
                return Long.parseLong(next());
            }

            double nextDouble() {
                return Double.parseDouble(next());
            }

            String nextLine() {
                String str = "";
                try {
                    str = br.readLine();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                return str;
            }

        }
    }