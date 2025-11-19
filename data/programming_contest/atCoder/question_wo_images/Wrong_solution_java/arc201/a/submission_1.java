import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine());
            long total = 0;

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                long A = Long.parseLong(st.nextToken());
                long B = Long.parseLong(st.nextToken());
                long C = Long.parseLong(st.nextToken());

                long div1 = Math.min(A, B);
                long div2 = Math.min(B, C);
                total += Math.min(div1 + div2, B);
            }

            pw.println(total);
        }

        pw.flush();
        pw.close();
    }
}