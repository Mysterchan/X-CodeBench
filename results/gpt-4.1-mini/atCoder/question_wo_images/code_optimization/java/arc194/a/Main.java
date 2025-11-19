import java.io.*;
import java.util.*;

public class Main {
    static FastReader in = new FastReader();
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) {
        int n = in.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = in.nextInt();

        // We maintain a stack to simulate the sequence S.
        // For each element, we decide whether to append or delete the last element.
        // The optimal strategy:
        // - Always append the current element.
        // - If the last element in the stack is negative, pop it to maximize sum.
        // This works because deleting the last element is only beneficial if it is negative.

        Deque<Integer> stack = new ArrayDeque<>();
        long sum = 0;

        for (int val : arr) {
            stack.addLast(val);
            sum += val;

            // While the last element is negative, remove it to maximize sum
            while (!stack.isEmpty() && stack.peekLast() < 0) {
                int removed = stack.removeLast();
                sum -= removed;
            }
        }

        out.println(sum);
        out.flush();
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try { st = new StringTokenizer(br.readLine()); }
                catch (IOException e) { e.printStackTrace(); }
            }
            return st.nextToken();
        }

        int nextInt() { return Integer.parseInt(next()); }
    }
}