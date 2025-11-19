import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        final int MOD = 1000000007;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        
        int tc = Integer.parseInt(br.readLine());
        StringBuilder output = new StringBuilder();
        
        while(tc-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            // Calculate n and m directly
            long n = (long) (a + (k - 1) / 1);
            long m = (long) (b + (k - 1) / k);

            n %= MOD;
            m %= MOD;

            output.append(n).append(" ").append(m).append('\n');
        }
        
        pw.print(output);
        pw.close();
    }
}