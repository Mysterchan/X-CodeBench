import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        solve(br, out);
        out.close();
    }

    static void solve(BufferedReader br, PrintWriter out) throws IOException {
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] p = new int[n];
        int[] pos = new int[n];
        
        for (int i = 0; i < n; i++) {
            p[i] = Integer.parseInt(st.nextToken()) - 1;
            pos[p[i]] = i;
        }
        
        long ans = 0;
        
        for (int target = 0; target < n; target++) {
            int currentPos = pos[target];
            
            if (currentPos == target) continue;
            
            // Move element from currentPos to target
            // We need to bubble it left
            for (int i = currentPos; i > target; i--) {
                // Swap position i-1 and i (1-indexed cost is i)
                ans += i;
                
                // Update positions
                int elem = p[i];
                int leftElem = p[i-1];
                
                p[i] = leftElem;
                p[i-1] = elem;
                
                pos[elem] = i - 1;
                pos[leftElem] = i;
            }
        }
        
        out.println(ans);
    }
}