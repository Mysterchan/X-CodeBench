import java.io.IOException;
import java.io.InputStream;
import java.util.NoSuchElementException;

class Main {
    public static void main(String[] args) {
        FastScanner sc = new FastScanner();
        long N = sc.nextLong();
        int M = sc.nextInt();
        int A = sc.nextInt();
        int B = sc.nextInt();

        // Create an array to mark bad squares
        boolean[] bad = new boolean[(int) N + 1];

        // Read the bad ranges and mark them
        for (int i = 0; i < M; i++) {
            long L = sc.nextLong();
            long R = sc.nextLong();
            for (long j = L; j <= R; j++) {
                bad[(int) j] = true;
            }
        }

        // BFS or simple iteration to check if we can reach N
        boolean[] reachable = new boolean[(int) N + 1];
        reachable[1] = true;

        for (int i = 1; i < N; i++) {
            if (reachable[i]) {
                for (int step = A; step <= B; step++) {
                    int nextSquare = i + step;
                    if (nextSquare <= N && !bad[nextSquare]) {
                        reachable[nextSquare] = true;
                    }
                }
            }
        }

        System.out.println(reachable[(int) N] ? "Yes" : "No");
    }
}

class FastScanner {
    private final InputStream in = System.in;
    private final byte[] buffer = new byte[1024];
    private int ptr = 0;
    private int buflen = 0;

    private boolean hasNextByte() {
        if (ptr < buflen) return true;
        ptr = 0;
        try {
            buflen = in.read(buffer);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return buflen > 0;
    }

    private int readByte() {
        if (hasNextByte()) return buffer[ptr++];
        else return -1;
    }

    private boolean isPrintableChar(int c) {
        return 33 <= c && c <= 126;
    }

    public boolean hasNext() {
        while (hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++;
        return hasNextByte();
    }

    public String next() {
        if (!hasNext()) throw new NoSuchElementException();
        StringBuilder sb = new StringBuilder();
        int b = readByte();
        while (isPrintableChar(b)) {
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }

    public long nextLong() {
        if (!hasNext()) throw new NoSuchElementException();
        long n = 0;
        boolean minus = false;
        int b = readByte();
        if (b == '-') {
            minus = true;
            b = readByte();
        }
        while (b >= '0' && b <= '9') {
            n = n * 10 + (b - '0');
            b = readByte();
        }
        return minus ? -n : n;
    }

    public int nextInt() {
        return (int) nextLong();
    }
}