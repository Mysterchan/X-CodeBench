import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        
        for (int z = 0; z < t; z++) {
            String[] sa = br.readLine().split(" ");
            int n = Integer.parseInt(sa[0]);
            int m = Integer.parseInt(sa[1]);
            
            int[] a = new int[n];
            int[] b = new int[n];
            
            sa = br.readLine().split(" ");
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(sa[i]);
            }
            
            sa = br.readLine().split(" ");
            for (int i = 0; i < n; i++) {
                b[i] = Integer.parseInt(sa[i]);
            }

            Arrays.sort(a);
            Arrays.sort(b);

            int ans = 0;
            for (int i = 0; i < n; i++) {
                int modSum = (a[i] + b[n - 1 - i]) % m;
                ans = Math.max(ans, modSum);
            }
            
            sb.append(ans).append('\n');
        }
        br.close();
        System.out.print(sb.toString());
    }
}