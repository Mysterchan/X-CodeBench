import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br;
    static PrintWriter out;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(new OutputStreamWriter(System.out));
        int T = readInt();
        for (int t = 0; t < T; t++) {
            int H = readInt();
            int W = readInt();
            String S = readLine();

            int dCount = 0;
            int rCount = 0;
            for (char c : S.toCharArray()) {
                if (c == 'D') dCount++;
                else if (c == 'R') rCount++;
            }

            int ans = (H - dCount) * (W - rCount);
            out.println(ans);
        }
        out.close();
    }

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine().trim());
        return st.nextToken();
    }

    static int readInt() throws IOException {
        return Integer.parseInt(next());
    }

    static String readLine() throws IOException {
        return br.readLine().trim();
    }
}