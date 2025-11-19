import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.Comparator;

public class Main {

    static class Block {
        int x;
        long y;
        int id;
        Block(int x, long y, int id) { this.x = x; this.y = y; this.id = id; }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());

        Block[] blocks = new Block[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            long y = Long.parseLong(st.nextToken());
            blocks[i] = new Block(x, y, i + 1);
        }

        Arrays.sort(blocks, (a, b) -> {
            if (a.x != b.x) return Integer.compare(a.x, b.x);
            return Long.compare(a.y, b.y);
        });

        int[] y_rest = new int[N + 1];
        int[] count = new int[N + 1];
        int current_col = -1;
        int k = 1;
        for (int i = 0; i < N; i++) {
            if (blocks[i].x != current_col) {
                current_col = blocks[i].x;
                k = 1;
            }
            y_rest[blocks[i].id] = k;
            count[k]++;
            k++;
        }

        int t_clear = 0;
        int r = 1;
        while (r <= N && count[r] == W) {
            t_clear++;
            r++;
        }

        int Q = Integer.parseInt(br.readLine());
        for (int q = 0; q < Q; q++) {
            st = new StringTokenizer(br.readLine());
            int T = Integer.parseInt(st.nextToken());
            int A = Integer.parseInt(st.nextToken());

            int rest_row = y_rest[A];

            if (T == 1) {
                out.println("Yes");
                continue;
            }

            int T_event = T - 1;

            if (rest_row > t_clear) {

                out.println("Yes");
            } else {

                if (T_event < rest_row) {
                    out.println("Yes");
                } else {
                    out.println("No");
                }
            }
        }
        out.flush();
    }
}