import java.io.*;
import java.util.*;

public class Main {
    static class FastScanner {
        private final InputStream in = System.in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;
        private int read() throws IOException {
            if (ptr >= len) { len = in.read(buffer); ptr = 0; if (len <= 0) return -1; }
            return buffer[ptr++];
        }
        int nextInt() throws IOException {
            int c; do { c = read(); } while (c <= ' ');
            boolean neg = c == '-'; if (neg) c = read();
            int x = 0; while (c > ' ') { x = x * 10 + (c - '0'); c = read(); }
            return neg ? -x : x;
        }
    }

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();
        int N = fs.nextInt();
        int L = fs.nextInt();

        int[] pos = new int[N + 1];
        pos[1] = 0;
        for (int i = 2; i <= N; i++) {
            pos[i] = (pos[i - 1] + fs.nextInt()) % L;
        }

        // If L is not divisible by 3, no equilateral triangle can be formed
        if (L % 3 != 0) {
            System.out.println(0);
            return;
        }

        int step = L / 3;

        // Map from position to list of indices at that position
        // Using HashMap for O(1) average lookup
        HashMap<Integer, ArrayList<Integer>> posMap = new HashMap<>();
        for (int i = 1; i <= N; i++) {
            posMap.computeIfAbsent(pos[i], k -> new ArrayList<>()).add(i);
        }

        long count = 0;

        // For each point a, find points b and c such that:
        // pos[b] = (pos[a] + step) % L
        // pos[c] = (pos[a] + 2*step) % L
        // Then count triples (a,b,c) with a < b < c
        for (int a = 1; a <= N; a++) {
            int pA = pos[a];
            int pB = (pA + step) % L;
            int pC = (pA + 2 * step) % L;

            ArrayList<Integer> listB = posMap.get(pB);
            ArrayList<Integer> listC = posMap.get(pC);

            if (listB == null || listC == null) continue;

            // Since indices in listB and listC are sorted by insertion order (increasing i),
            // we can use binary search to count how many b > a and c > b.

            // Find the first b in listB with b > a
            int idxB = lowerBound(listB, a + 1);
            if (idxB == listB.size()) continue; // no b > a

            // For each b > a, count c > b
            for (int iB = idxB; iB < listB.size(); iB++) {
                int b = listB.get(iB);
                // Find c in listC with c > b
                int idxC = lowerBound(listC, b + 1);
                if (idxC == listC.size()) continue;
                // Number of c > b is listC.size() - idxC
                count += (listC.size() - idxC);
            }
        }

        System.out.println(count);
    }

    // lowerBound: returns the index of the first element >= key
    static int lowerBound(ArrayList<Integer> list, int key) {
        int low = 0, high = list.size();
        while (low < high) {
            int mid = (low + high) >>> 1;
            if (list.get(mid) >= key) high = mid;
            else low = mid + 1;
        }
        return low;
    }
}