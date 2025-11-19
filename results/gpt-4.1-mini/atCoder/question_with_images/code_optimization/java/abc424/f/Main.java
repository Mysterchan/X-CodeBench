import java.io.*;
import java.util.*;

public class Main {
    static int N, Q;
    static int[] A, B;

    public static void main(String[] args) throws Exception {
        FastScanner sc = new FastScanner();
        N = sc.nextInt();
        Q = sc.nextInt();
        A = new int[Q];
        B = new int[Q];
        for (int i = 0; i < Q; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            if (a > b) {
                int tmp = a;
                a = b;
                b = tmp;
            }
            A[i] = a;
            B[i] = b;
        }

        // We will maintain a stack of intervals representing drawn chords.
        // Each chord is represented by its endpoints (a,b) with a < b.
        // The key insight:
        // Two chords (a,b) and (c,d) intersect if and only if:
        // a < c < b < d or c < a < d < b
        // Since all points are distinct, and chords are on a circle,
        // we can maintain a stack of intervals sorted by their start point.
        // When adding a new chord, it must not intersect any existing chord.
        // The stack will maintain intervals in increasing order of start point,
        // and the intervals are nested or disjoint without intersection.
        //
        // Algorithm:
        // For each query (a,b):
        // - While stack top's end point is less than b, pop from stack.
        // - If stack is empty or top's end point < a, push (a,b) and print "Yes"
        // - Else print "No"
        //
        // This works because the chords drawn form a non-crossing matching,
        // and the stack simulates the nesting of intervals.

        Deque<int[]> stack = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < Q; i++) {
            int a = A[i];
            int b = B[i];

            // Pop intervals that end before b
            while (!stack.isEmpty() && stack.peek()[1] < b) {
                stack.pop();
            }

            if (stack.isEmpty() || stack.peek()[1] < a) {
                // No intersection, draw chord
                stack.push(new int[]{a, b});
                sb.append("Yes\n");
            } else {
                // Intersecting chord exists
                sb.append("No\n");
            }
        }

        System.out.print(sb);
    }

    static class FastScanner {
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;
        private static final int BUFFER_SIZE = 1 << 16;

        public FastScanner() {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        private byte read() {
            try {
                if (bufferPointer == bytesRead) {
                    bytesRead = din.read(buffer, 0, BUFFER_SIZE);
                    if (bytesRead == -1) return -1;
                    bufferPointer = 0;
                }
                return buffer[bufferPointer++];
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }

        public int nextInt() {
            int ret = 0;
            byte c = read();
            while (c <= ' ') c = read();
            boolean neg = (c == '-');
            if (neg) c = read();
            do {
                ret = ret * 10 + c - '0';
                c = read();
            } while (c > ' ');
            return neg ? -ret : ret;
        }
    }
}