import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        FastScanner sc = new FastScanner();
        int t = sc.nextInt();
        PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
        while (t-- > 0) {
            int n = sc.nextInt();
            int[][] arr = new int[n][2];
            for(int i=0; i<n; i++){
                arr[i][0] = sc.nextInt();
                arr[i][1] = sc.nextInt();
            }
            if(n==1){
                out.write("1\n");
                continue;
            }
            Arrays.sort(arr, (x, y) -> {
                if(x[0] != y[0]){
                    return Integer.compare(x[0], y[0]);
                }
                return Integer.compare(x[1], y[1]);
            });
            long result = solve(arr, true, n);
            result = Math.min(result, solve(arr, false, n));

            Arrays.sort(arr, (x, y) -> {
                if(x[1] != y[1]){
                    return Integer.compare(x[1], y[1]);
                }
                return Integer.compare(x[0], y[0]);
            });
            result = Math.min(result, solve(arr, false, n));
            result = Math.min(result, solve(arr, true, n));

            result = Math.max(result, n);
            out.write(result + "\n");

        }

        out.flush();
        out.close();
        sc.close();
    }

    private static long solve(int[][] arr, boolean flag, int n){
        int min = flag ? 0 : 1;
        int max = flag ? n-1 : n;
        int minX = Integer.MAX_VALUE;
        int maxX = Integer.MIN_VALUE;
        int minY = Integer.MAX_VALUE;
        int maxY = Integer.MIN_VALUE;
        for(int i=min; i<max; i++){
            minX = Math.min(minX, arr[i][0]);
            maxX = Math.max(maxX, arr[i][0]);
            minY = Math.min(minY, arr[i][1]);
            maxY = Math.max(maxY, arr[i][1]);
        }
        return (long)(maxX - minX + 1) * (long)(maxY - minY + 1);
    }
}
class FastScanner {
    BufferedReader br;
    StringTokenizer st;

    public FastScanner() {
        br = new BufferedReader(new InputStreamReader(System.in));
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }

    public long nextLong() {
        return Long.parseLong(next());
    }

    public String nextLine() {
        String str = "";
        try {
            str = br.readLine();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return str;
    }

    public double nextDouble() {
        return Double.parseDouble(next());
    }

    public String next() {
        while (st == null || !st.hasMoreElements()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return st.nextToken();
    }

    public void close() {
        try {
            br.close();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
