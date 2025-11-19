import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] A = new int[N + 2];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        // diff array for range increments of received gifts
        long[] diff = new long[N + 3];
        long currAdd = 0;

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            // accumulate how many gifts i has received by now
            currAdd += diff[i];
            long Ci = A[i] + currAdd;             // stones after receiving at own adulthood
            long Di = Math.min(Ci, N - i);       // how many stones it will give away
            long Bi = Ci - Di;                   // final stones after giving

            if (i > 1) sb.append(' ');
            sb.append(Bi);

            if (Di > 0) {
                // schedule Di gifts to next Di new adults
                int l = i + 1;
                int r = i + (int)Di;
                diff[l] += 1;
                diff[r + 1] -= 1;
            }
        }

        System.out.println(sb.toString());
    }
}