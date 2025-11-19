import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));

        int tt = Integer.parseInt(in.readLine());
        while (tt-- > 0) {
            StringTokenizer st = new StringTokenizer(in.readLine());
            int s = Integer.parseInt(st.nextToken()), k = Integer.parseInt(st.nextToken());
            if (s > k * k) {
                if (s % k == 0) {
                    out.println(k);
                } else {
                    out.println(Math.max(1, k - 2));
                }
                continue;
            }
            boolean[] v = new boolean[s + 1];
            v[0] = true;
            int bu = k;
            while (bu > 1) {
                boolean[] vn = new boolean[s + 1];
                if ((k - bu & 1) == 0) {
                    for (int i = bu; i <= s; i++) {
                        vn[i] = vn[i - bu] | v[i - bu];
                    }
                } else {
                    for (int i = s - bu; i >= 0; i--) {
                        vn[i] = vn[i + bu] | v[i + bu];
                    }
                }
                if (vn[s]) {
                    break;
                }
                v = vn;
                bu--;
            }
            out.println(bu);
        }
        out.flush();
    }

}
