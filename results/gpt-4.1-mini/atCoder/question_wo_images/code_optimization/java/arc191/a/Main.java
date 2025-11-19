import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // Use BufferedReader and BufferedWriter for fast IO
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        char[] s = br.readLine().toCharArray();
        char[] t = br.readLine().toCharArray();
        
        // Sort t in descending order to get the largest digits first
        Arrays.sort(t);
        // Reverse t to descending order
        for (int i = 0; i < m / 2; i++) {
            char temp = t[i];
            t[i] = t[m - 1 - i];
            t[m - 1 - i] = temp;
        }
        
        int idx = 0;
        // Replace digits in s with digits from t if t[idx] > s[i]
        for (int i = 0; i < n && idx < m; i++) {
            if (t[idx] > s[i]) {
                s[i] = t[idx];
                idx++;
            }
        }
        
        bw.write(s);
        bw.newLine();
        bw.flush();
    }
}