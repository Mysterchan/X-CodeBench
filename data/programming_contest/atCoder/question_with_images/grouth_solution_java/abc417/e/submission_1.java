import java.io.IOException;
import java.io.InputStream;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int T = fs.nextInt();

        StringBuilder sb = new StringBuilder();

        while (T-- > 0) {
            int N = fs.nextInt();
            int M = fs.nextInt();
            int X = fs.nextInt();
            int Y = fs.nextInt();

            List<List<Integer>> G = new ArrayList<>();
            for (int i = 0; i <= N; i++) G.add(new ArrayList<>());

            for (int i = 0; i < M; i++) {
                int U = fs.nextInt();
                int V = fs.nextInt();
                G.get(U).add(V);
                G.get(V).add(U);
            }

            for (int i = 1; i <= N; i++) G.get(i).sort(Comparator.naturalOrder());

            List<Integer> path = new ArrayList<>();
            boolean[] used = new boolean[N + 1];

            int cur = X;
            path.add(cur);
            used[cur] = true;

            while (cur != Y) {
                for (int v : G.get(cur)) {
                    if (used[v]) continue;

                    boolean[] visited2 = used.clone();
                    Deque<Integer> deque = new ArrayDeque<>();

                    deque.add(v);
                    visited2[v] = true;

                    boolean reach = false;

                    while (!deque.isEmpty()) {
                        int a = deque.poll();

                        if (a == Y) {
                            reach = true;
                            break;
                        }

                        for (int w : G.get(a)) {
                            if (!visited2[w]) {
                                deque.add(w);
                                visited2[w] = true;
                            }
                        }
                    }

                    if (reach) {
                        used[v] = true;
                        path.add(v);
                        cur = v;
                        break;
                    }
                }
            }

            int s = path.size();
            for (int i = 0; i < s; i++) sb.append(path.get(i)).append((i == (s - 1)) ? "\n" : " ");
        }

        System.out.print(sb);
    }

    static class FastScanner {
        private final InputStream in = System.in;
        private final byte[] buffer = new byte[1024];
        private int ptr = 0;
        private int bufLen = 0;

        private boolean hasNextByte() {
            if (ptr < bufLen) {
                return true;
            } else {
                ptr = 0;

                try {
                    bufLen = in.read(buffer);
                } catch (IOException e) {
                    e.printStackTrace(System.err);
                }

                return bufLen > 0;
            }
        }
        private int readByte() { if (hasNextByte()) return buffer[ptr++]; else return -1;}
        private static boolean isPrintableChar(int c) { return 33 <= c && c <= 126;}
        public boolean hasNext() { while(hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++; return hasNextByte();}
        public String next() {
            if (!hasNext()) throw new NoSuchElementException();
            StringBuilder sb = new StringBuilder();
            int b = readByte();
            while(isPrintableChar(b)) {
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

            if (b < '0' || '9' < b) throw new NumberFormatException();

            while (true) {
                if ('0' <= b && b <= '9') {
                    n *= 10;
                    n += b - '0';
                }else if(b == -1 || !isPrintableChar(b)){
                    return minus ? -n : n;
                }else{
                    throw new NumberFormatException();
                }
                b = readByte();
            }
        }
        public int nextInt() {
            long nl = nextLong();
            if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE) throw new NumberFormatException();
            return (int) nl;
        }
        public double nextDouble() { return Double.parseDouble(next());}
    }
}