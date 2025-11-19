import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        FastReader fr = new FastReader();

        int n = fr.nextInt();
        int k = fr.nextInt();

        long[] a = new long[n];
        long[] b = new long[n];
        long[] c = new long[n];

        for (int i = 0; i < n; i++) a[i] = fr.nextLong();
        for (int i = 0; i < n; i++) b[i] = fr.nextLong();
        for (int i = 0; i < n; i++) c[i] = fr.nextLong();

        // Sort the arrays in descending order
        Arrays.sort(a);
        Arrays.sort(b);
        Arrays.sort(c);
        reverseArray(a);
        reverseArray(b);
        reverseArray(c);

        PriorityQueue<Long> pq = new PriorityQueue<>();

        // Use a set to avoid duplicates in index pairs
        Set<String> visited = new HashSet<>();

        // Start with the largest indices
        long maxCost = a[0] * b[0] + b[0] * c[0] + c[0] * a[0];
        pq.offer(maxCost);
        visited.add("0_0_0");

        while (pq.size() < k) {
            long cost = pq.poll();

            // Get the indices for the current max cost
            for (int i = 0; i < 3; i++) {
                int f = (i == 0) ? 0 : -1;
                int s = (i == 1) ? 0 : -1;
                int p = (i == 2) ? 0 : -1;

                // Generate new costs based on incrementing one of the indices
                if (f == 0) { 
                    if (s < n - 1) { // Increment B
                        String key = "0_" + (s + 1) + "_" + 0;
                        long newCost = a[0] * b[s + 1] + b[s + 1] * c[0] + c[0] * a[0];
                        if (!visited.contains(key)) {
                            pq.offer(newCost);
                            visited.add(key);
                        }
                    } 
                    if (p < n - 1) { // Increment C
                        String key = "0_" + 0 + "_" + (p + 1);
                        long newCost = a[0] * b[0] + b[0] * c[p + 1] + c[p + 1] * a[0];
                        if (!visited.contains(key)) {
                            pq.offer(newCost);
                            visited.add(key);
                        }
                    }
                } else if (s == 0) { 
                    if (f < n - 1) { // Increment A
                        String key = (f + 1) + "_0_" + 0;
                        long newCost = a[f + 1] * b[0] + b[0] * c[0] + c[0] * a[f + 1];
                        if (!visited.contains(key)) {
                            pq.offer(newCost);
                            visited.add(key);
                        }
                    } 
                    if (p < n - 1) { // Increment C
                        String key = "0_" + 0 + "_" + (p + 1);
                        long newCost = a[0] * b[0] + b[0] * c[p + 1] + c[p + 1] * a[0];
                        if (!visited.contains(key)) {
                            pq.offer(newCost);
                            visited.add(key);
                        }
                    }
                } else if (p == 0) { 
                    if (f < n - 1) { // Increment A
                        String key = (f + 1) + "_" + 0 + "_" + 0;
                        long newCost = a[f + 1] * b[0] + b[0] * c[0] + c[0] * a[f + 1];
                        if (!visited.contains(key)) {
                            pq.offer(newCost);
                            visited.add(key);
                        }
                    } 
                    if (s < n - 1) { // Increment B
                        String key = "0_" + (s + 1) + "_0";
                        long newCost = a[0] * b[s + 1] + b[s + 1] * c[0] + c[0] * a[0];
                        if (!visited.contains(key)) {
                            pq.offer(newCost);
                            visited.add(key);
                        }
                    }
                }
            }
        }

        // Output the K-th largest
        List<Long> resultList = new ArrayList<>(pq);
        Collections.sort(resultList, Collections.reverseOrder());

        System.out.println(resultList.get(k - 1));
    }

    private static void reverseArray(long[] array) {
        int left = 0, right = array.length - 1;
        while (left < right) {
            long temp = array[left];
            array[left] = array[right];
            array[right] = temp;
            left++;
            right--;
        }
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() { return Integer.parseInt(next()); }
        long nextLong() { return Long.parseLong(next()); }
        double nextDouble() { return Double.parseDouble(next()); }
        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}