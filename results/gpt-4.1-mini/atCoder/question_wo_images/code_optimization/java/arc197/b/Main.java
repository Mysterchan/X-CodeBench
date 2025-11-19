import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        FastReader sc = new FastReader();
        PrintWriter out = new PrintWriter(System.out);

        int T = sc.nextInt();
        while (T-- > 0) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            long sum = 0;
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
                sum += arr[i];
            }

            Arrays.sort(arr);

            // If all elements are equal, no element can be strictly greater than average
            if (arr[0] == arr[n - 1]) {
                out.println(0);
                continue;
            }

            // We want to find the longest suffix (from some index i to end)
            // such that the average of that subsequence is less than arr[i]
            // Because all elements in suffix are >= arr[i], the average is between arr[i] and arr[n-1].
            // For the score (count of elements > average) to be maximized,
            // we want as many elements strictly greater than average as possible.
            // The best subsequence is a suffix starting at some index i.

            // Precompute prefix sums for O(1) range sum queries
            long[] prefix = new long[n + 1];
            for (int i = 0; i < n; i++) {
                prefix[i + 1] = prefix[i] + arr[i];
            }

            int ans = 0;
            // Iterate over possible start indices of suffix
            // For each i, check if average of arr[i..n-1] < arr[i]
            // average = (prefix[n] - prefix[i]) / (n - i)
            // condition: average < arr[i] => (prefix[n] - prefix[i]) < arr[i] * (n - i)
            for (int i = 0; i < n; i++) {
                long sumSub = prefix[n] - prefix[i];
                int length = n - i;
                if (sumSub < (long) arr[i] * length) {
                    // number of elements strictly greater than average is count of elements > average
                    // Since arr[i] > average and arr[i..n-1] are sorted ascending,
                    // all elements from i+1 to n-1 are >= arr[i], so all except arr[i] itself are > average
                    // But arr[i] might be equal to average? No, average < arr[i], so arr[i] > average
                    // So all elements in suffix are > average except possibly some equal to arr[i]
                    // But since arr[i] is the smallest in suffix, all elements >= arr[i]
                    // So count of elements > average = length of suffix
                    // But the problem counts strictly greater than average, so all elements in suffix are > average
                    // So score = length of suffix
                    ans = length;
                    break; // since suffix length decreases as i increases, first found is max
                }
            }

            out.println(ans);
        }

        out.flush();
        out.close();
    }

    // Fast input reader
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() throws Exception {
            while (st == null || !st.hasMoreTokens()) {
                String line = br.readLine();
                if (line == null) return null;
                st = new StringTokenizer(line);
            }
            return st.nextToken();
        }

        int nextInt() throws Exception {
            return Integer.parseInt(next());
        }
    }
}