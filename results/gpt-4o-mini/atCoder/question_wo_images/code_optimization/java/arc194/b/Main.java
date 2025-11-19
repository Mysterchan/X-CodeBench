import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] p = new long[n];
        for (int i = 0; i < n; i++) {
            p[i] = Long.parseLong(st.nextToken()) - 1;
        }

        long[] position = new long[n];
        for (int i = 0; i < n; i++) {
            position[(int)p[i]] = i;
        }
        
        long ans = 0;
        for (int i = 0; i < n; i++) {
            while (position[i] != i) {
                int j = (int) position[i];
                ans += j + 1; // cost of swapping
                // Swap in position array
                long temp = position[(int) p[j - 1]];
                position[(int) p[j - 1]] = j;
                position[(int) p[j]] = temp;

                // Swap values in the permutation
                long tempP = p[j];
                p[j] = p[j - 1];
                p[j - 1] = tempP;
            }
        }
        
        out.println(ans);
        out.close();
    }
}