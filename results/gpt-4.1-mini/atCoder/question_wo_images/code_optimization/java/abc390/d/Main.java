import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {
    // Function to compute the XOR basis of the array
    // Returns the size of the basis
    static int buildXorBasis(long[] arr, long[] basis) {
        int size = 0;
        for (long x : arr) {
            for (int i = size - 1; i >= 0; i--) {
                x = Math.min(x, x ^ basis[i]);
            }
            if (x > 0) {
                // Insert x into basis in descending order
                int i = size - 1;
                while (i >= 0 && basis[i] < x) {
                    basis[i + 1] = basis[i];
                    i--;
                }
                basis[i + 1] = x;
                size++;
            }
        }
        return size;
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

        // The problem reduces to finding the number of distinct XOR values
        // that can be formed by XORing any subset of the basis vectors.
        // The number of distinct XOR values is 2^(size of basis).

        long[] basis = new long[N];
        int basisSize = buildXorBasis(arr, basis);

        // Calculate 2^basisSize
        long result = 1L << basisSize;

        pw.println(result);
        pw.close();
    }
}