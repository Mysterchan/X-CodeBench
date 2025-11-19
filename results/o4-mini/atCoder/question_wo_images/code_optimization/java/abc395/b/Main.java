import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int layer = Math.min(Math.min(i, j), Math.min(N - 1 - i, N - 1 - j));
                sb.append((layer % 2 == 0) ? '#' : '.');
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }
}