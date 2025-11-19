import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        // Since A_i ≤ 10^6, we allocate an array of size 1e6+1 to track last positions.
        int[] last = new int[1_000_001];
        Arrays.fill(last, -1);

        int minLen = N + 1;
        for (int i = 0; i < N; i++) {
            int x = Integer.parseInt(st.nextToken());
            if (last[x] != -1) {
                // update answer with the length between two occurrences + 1
                minLen = Math.min(minLen, i - last[x] + 1);
            }
            last[x] = i;
        }

        System.out.println(minLen > N ? -1 : minLen);
    }
}