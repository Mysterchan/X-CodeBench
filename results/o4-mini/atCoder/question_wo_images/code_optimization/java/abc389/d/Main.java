import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int rIn = Integer.parseInt(br.readLine());
        long R = rIn;
        long limit = 4 * R * R;
        long sum = 0;
        long j = R;
        for (long i = 1; ; i++) {
            long xi = 2 * i + 1;
            if (xi * xi > limit) break;
            while (j >= 0) {
                long yj = 2 * j + 1;
                if (xi * xi + yj * yj <= limit) break;
                j--;
            }
            if (j < 0) break;
            sum += j + 1;
        }
        long answer = sum * 4 + 1;
        System.out.println(answer);
    }
}