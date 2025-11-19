import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class Main {
    static Set<Long> results = new HashSet<>();
    static Set<String> visited = new HashSet<>();
    
    public static void solve(long[] arr) {
        String state = Arrays.toString(arr);
        if (visited.contains(state)) return;
        visited.add(state);
        
        long xor = 0;
        for (long val : arr) {
            xor ^= val;
        }
        results.add(xor);
        
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            if (arr[i] == 0) continue;
            for (int j = 0; j < n; j++) {
                if (i == j || arr[j] == 0) continue;
                
                long temp = arr[i];
                arr[i] = 0;
                arr[j] += temp;
                
                solve(arr);
                
                arr[j] -= temp;
                arr[i] = temp;
            }
        }
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] arr = new long[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }
        
        solve(arr);
        
        pw.println(results.size());
        pw.close();
    }
}