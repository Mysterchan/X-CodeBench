import java.io.IOException;
import java.io.InputStream;
import java.util.NoSuchElementException;

class Main implements Runnable {
    public static void main(String[] args) {
        new Thread(null, new Main(), "", 1024 * 1024 * 1024).start();
    }

    public void run() {
        FastScanner sc = FastScanner.getInstance();
        
        long N = sc.nextLong();
        int M = sc.nextInt();
        int A = sc.nextInt();
        int B = sc.nextInt();
        long[] L = new long[M];
        long[] R = new long[M];
        for (int i = 0; i < M; ++i) {
            L[i] = sc.nextLong();
            R[i] = sc.nextLong();
        }
        
        boolean[] reach = new boolean[21];
        reach[0] = true;
        
        long cur = 1;
        for (int i = 0; i < M; ++i) {
            int j = i;
            while (j + 1 < M && R[j] == L[j + 1] - 1) ++j;
            
            long gap = L[i] - cur - 1;
            if (gap >= B) {
                for (int k = 0; k < B; ++k) reach[k] = true;
            } else if (gap > 0) {
                boolean[] nreach = new boolean[21];
                for (int k = 0; k < 21; ++k) {
                    if (reach[k]) {
                        for (int d = A; d <= B && k + d < 21; ++d) {
                            nreach[k + d] = true;
                        }
                    }
                }
                for (int t = 1; t < gap; ++t) {
                    boolean[] tmp = new boolean[21];
                    for (int k = 0; k < 21; ++k) {
                        if (nreach[k]) {
                            for (int d = A; d <= B && k + d < 21; ++d) {
                                tmp[k + d] = true;
                            }
                        }
                    }
                    nreach = tmp;
                }
                reach = nreach;
            }
            
            cur = L[i] - 1;
            int w = (int)(R[j] - L[i] + 1);
            if (w >= 20) {
                System.out.println("No");
                return;
            }
            
            boolean[] nreach = new boolean[21];
            for (int k = A; k <= B; ++k) {
                int id = k - w - 1;
                if (id >= 0 && id < 21) nreach[0] |= reach[id];
            }
            for (int k = 0; k < 21; ++k) {
                if (k + 1 + w < 21) nreach[k + 1 + w] = reach[k];
            }
            reach = nreach;
            cur = R[j] + 1;
            i = j;
        }
        
        long gap = N - cur;
        if (gap >= B) {
            System.out.println("Yes");
            return;
        }
        
        for (int t = 0; t < gap; ++t) {
            boolean[] nreach = new boolean[21];
            for (int k = 0; k < 21; ++k) {
                if (reach[k]) {
                    for (int d = A; d <= B && k + d < 21; ++d) {
                        nreach[k + d] = true;
                    }
                }
            }
            reach = nreach;
        }
        
        System.out.println(reach[0] ? "Yes" : "No");
    }
}

class FastScanner {
    private static FastScanner instance = null;
    private final InputStream in = System.in;
    private final byte[] buffer = new byte[1024];
    private int ptr = 0;
    private int buflen = 0;

    private FastScanner() {}

    public static FastScanner getInstance() {
        if (instance == null) instance = new FastScanner();
        return instance;
    }

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
        return hasNextByte() ? buffer[ptr++] : -1;
    }

    private boolean isPrintableChar(int c) {
        return 33 <= c && c <= 126;
    }

    public boolean hasNext() {
        while (hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++;
        return hasNextByte();
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