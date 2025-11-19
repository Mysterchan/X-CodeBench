import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        FastScanner sc = new FastScanner();
        int N = sc.nextInt();
        int[] P = new int[N];
        for (int i = 0; i < N; i++) {
            P[i] = sc.nextInt() - 1; // Convert to zero-indexed
        }

        // Create the final output array
        int[] ans = new int[N];
        
        // We use a list to manage positions
        List<Integer> positions = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            positions.add(i); // Initialize positions
        }

        // Fill the answer array using the positions
        for (int i = N - 1; i >= 0; i--) {
            int idx = P[i];
            ans[positions.get(idx)] = i + 1; // Store i+1 because we want results from 1 to N
            positions.remove(idx); // Remove used position
        }

        // Print the output array
        for (int i = 0; i < N; i++) {
            System.out.print(ans[i] + " ");
        }
        System.out.println();
    }

    public static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
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

        public int nextInt() {
            return Integer.parseInt(next());
        }
    }
}