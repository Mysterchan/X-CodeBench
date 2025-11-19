import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner sc = new FastScanner();
        int n = sc.nextInt();
        int q = sc.nextInt();
        
        // To keep track of the latest drawn segments
        boolean[] drawn = new boolean[n + 1];
        StringBuilder sb = new StringBuilder();

        // Process each query
        for (int i = 0; i < q; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            
            // Normalize the points if they overflow
            if (a > b) {
                int temp = a;
                a = b;
                b = temp;
            }

            boolean canDraw = true;

            // Check for intersections
            for (int j = a; j < b; j++) {
                if (drawn[j]) {
                    canDraw = false;
                    break;
                }
            }
            // If can draw, mark the segment as drawn
            if (canDraw) {
                sb.append("Yes\n");
                for (int j = a; j < b; j++) {
                    drawn[j] = true; // Mark all points in between as drawn
                }
            } else {
                sb.append("No\n");
            }
        }
        System.out.print(sb);
    }
}

class FastScanner {
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

    public String next() {
        byte b = read();

        while (isSpaceChar(b)) {
            b = read();
        }
        StringBuilder sb = new StringBuilder();
        while (!isSpaceChar(b)) {
            sb.append((char) b);
            b = read();
        }
        return sb.toString();
    }

    public int nextInt() {
        int ret = 0;
        byte c = read();
        while (isSpaceChar(c)) c = read();
        boolean neg = (c == '-');
        if (neg) c = read();
        do {
            ret = ret * 10 + c - '0';
            c = read();
        } while (!isSpaceChar(c));
        return neg ? -ret : ret;
    }

    private boolean isSpaceChar(byte c) {
        return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
    }

    public void close() {
        try {
            if (din != null) din.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}