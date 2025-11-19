import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] A = new int[N];
        st = new StringTokenizer(br.readLine());

        int maxVal = 0;

        int[] freq = new int[1000001];
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
            freq[A[i]]++;
            maxVal = Math.max(maxVal, A[i]);
        }

        int[] count = new int[maxVal + 1];
        for (int g = 1; g <= maxVal; g++) {
            for (int v = g; v <= maxVal; v += g) {
                count[g] += freq[v];
            }
        }

        int[] ans_for_val = new int[maxVal + 1];

        for (int g = maxVal; g >= 1; g--) {

            if (count[g] < K) {
                continue;
            }

            for (int v = g; v <= maxVal; v += g) {
                if (ans_for_val[v] == 0) {
                    ans_for_val[v] = g;
                }
            }
        }

        for (int i = 0; i < N; i++) {
            out.println(ans_for_val[A[i]]);
        }

        out.flush();
    }
}