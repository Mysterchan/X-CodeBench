import java.util.*;
import java.io.*;

public class Main {
    static FastScanner fs = new FastScanner();
    
    public static void main(String[] args) {
        PrintWriter out = new PrintWriter(System.out);
        int t = fs.nextInt();
        
        while (t-- > 0) {
            int n = fs.nextInt();
            ArrayList<int[]> arrays = new ArrayList<>();
            int maxLength = 0;
            
            for (int i = 0; i < n; i++) {
                int k = fs.nextInt();
                int[] array = new int[k];
                for (int j = 0; j < k; j++) {
                    array[j] = fs.nextInt();
                }
                arrays.add(array);
                maxLength = Math.max(maxLength, k);
            }
            
            int[] result = new int[maxLength];
            boolean[] used = new boolean[n];
            Arrays.fill(result, Integer.MAX_VALUE);

            for (int row = 0; row < maxLength; row++) {
                for (int i = 0; i < n; i++) {
                    if (used[i]) continue; // Skip used rows
                    int[] array = arrays.get(i);
                    if (row < array.length) {
                        result[row] = Math.min(result[row], array[row]);
                    }
                }
                // Mark the smallest value's originating row as used
                for (int i = 0; i < n; i++) {
                    if (used[i]) continue;
                    int[] array = arrays.get(i);
                    if (row < array.length && result[row] == array[row]) {
                        used[i] = true;
                        break;
                    }
                }
            }
            
            for (int v : result) {
                out.print(v + " ");
            }
            out.println();
        }
        out.close();
    }

    static class FastScanner {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");
        
        String next() {
            while (!st.hasMoreTokens())
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }
}