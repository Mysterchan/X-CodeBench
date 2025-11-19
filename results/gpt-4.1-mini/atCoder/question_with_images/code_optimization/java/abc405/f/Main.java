import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        // Fast IO setup
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // We will store the M segments (all even points)
        // and process them to build a data structure for fast queries.

        // Since points are on a circle from 1 to 2N,
        // and segments connect even points only,
        // we can map points to [1..2N] and handle intervals on circle.

        // We'll represent each segment as an interval on the circle.
        // For each segment (a,b), a < b, the segment covers the arc from a to b clockwise.
        // The query segment (c,d) is between odd points.
        // The problem reduces to counting how many segments intersect the query segment.

        // Key insight:
        // Two chords (segments) on a circle intersect if and only if their endpoints interleave.
        // i.e. for segments (a,b) and (c,d) with a<b and c<d,
        // they intersect if (a < c < b < d) or (c < a < d < b) in circular order.

        // We can fix the order by mapping points to [1..2N] and consider intervals on a line by "cutting" the circle at some point.

        // Approach:
        // 1. Normalize all segments so that a < b.
        // 2. Sort segments by their start point a.
        // 3. For queries, also normalize c < d.
        // 4. For each query segment (c,d), count how many segments (a,b) satisfy:
        //    (a < c < b < d) or (c < a < d < b)
        //
        // Because the circle is linearized from 1 to 2N, we can handle wrap-around by doubling the circle:
        // Map points [1..2N] to [1..4N] by duplicating the circle.
        // Then all intervals can be represented as intervals on [1..4N].
        //
        // For each segment (a,b), we add interval [a,b] and [a+2N,b+2N].
        // For queries (c,d), we do the same.
        //
        // Then the intersection condition reduces to checking if intervals (a,b) and (c,d) interleave.
        //
        // We can process all segments and queries in this doubled space.

        // Implementation plan:
        // - For each segment (a,b), store (a,b) and (a+2N,b+2N).
        // - For queries (c,d), also consider (c,d) and (c+2N,d+2N).
        // - For each query, count how many segments intersect it.
        //
        // To count intersections efficiently:
        // - Sort segments by start point.
        // - For each query, we want to count how many segments (a,b) satisfy:
        //   a < c < b < d  OR  c < a < d < b
        //
        // This is equivalent to counting segments whose start and end points satisfy certain inequalities.
        //
        // We can process queries offline:
        // - Collect all segment intervals and queries.
        // - For each query, we want to count segments that start in certain ranges and end in certain ranges.
        //
        // We'll use a sweep line approach with coordinate compression and Fenwick tree (BIT).

        // Step 1: Read segments and store intervals
        int size = 2 * N;
        int doubleSize = 4 * N;

        int[] segStart = new int[M * 2];
        int[] segEnd = new int[M * 2];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if (a > b) {
                int tmp = a; a = b; b = tmp;
            }
            segStart[i] = a;
            segEnd[i] = b;
            // Add duplicated interval
            segStart[i + M] = a + size;
            segEnd[i + M] = b + size;
        }

        int Q = Integer.parseInt(br.readLine());

        // We'll store queries and their answers
        // For each query, we will create two intervals (c,d) and (c+2N,d+2N)
        // and count how many segments intersect with them.

        // We'll process queries offline:
        // For each query, we want to count how many segments intersect the query segment.
        // Intersection means endpoints interleave:
        // For intervals (a,b) and (c,d), they intersect if:
        // (a < c < b < d) or (c < a < d < b)

        // We can rewrite intersection condition as:
        // (a < c < b < d) or (c < a < d < b)
        // This is equivalent to:
        // (a < c and b > c and b < d) or (a > c and a < d and b > d)

        // So for each query interval (c,d), count segments (a,b) satisfying:
        // (a < c and b in (c,d)) or (a in (c,d) and b > d)

        // We'll process all intervals and queries together using coordinate compression and Fenwick tree.

        // Collect all points for compression
        int totalSegments = M * 2;
        int totalQueries = Q * 2;

        int[] allPoints = new int[totalSegments * 2 + totalQueries * 2];
        // segments: segStart and segEnd
        // queries: c,d and c+2N,d+2N

        // We'll store queries in arrays for processing
        int[] qC = new int[Q * 2];
        int[] qD = new int[Q * 2];

        for (int i = 0; i < M * 2; i++) {
            allPoints[i * 2] = segStart[i];
            allPoints[i * 2 + 1] = segEnd[i];
        }

        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            int c = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            if (c > d) {
                int tmp = c; c = d; d = tmp;
            }
            qC[i] = c;
            qD[i] = d;
            qC[i + Q] = c + size;
            qD[i + Q] = d + size;

            allPoints[totalSegments * 2 + i * 2] = qC[i];
            allPoints[totalSegments * 2 + i * 2 + 1] = qD[i];
            allPoints[totalSegments * 2 + (i + Q) * 2] = qC[i + Q];
            allPoints[totalSegments * 2 + (i + Q) * 2 + 1] = qD[i + Q];
        }

        // Coordinate compression
        int[] sortedPoints = allPoints.clone();
        Arrays.sort(sortedPoints);
        int uniqueCount = 0;
        for (int i = 0; i < sortedPoints.length; i++) {
            if (i == 0 || sortedPoints[i] != sortedPoints[i - 1]) {
                sortedPoints[uniqueCount++] = sortedPoints[i];
            }
        }

        // Function to get compressed index
        // 1-based indexing for Fenwick tree
        class Compressor {
            int[] arr;
            int size;

            Compressor(int[] a, int n) {
                arr = new int[n];
                System.arraycopy(a, 0, arr, 0, n);
                size = n;
            }

            int compress(int x) {
                int low = 0, high = size - 1;
                while (low <= high) {
                    int mid = (low + high) >>> 1;
                    if (arr[mid] == x) return mid + 1;
                    else if (arr[mid] < x) low = mid + 1;
                    else high = mid - 1;
                }
                return -1; // should not happen
            }
        }

        Compressor comp = new Compressor(sortedPoints, uniqueCount);

        // We will process queries offline using a sweep line on start points.
        // For each segment (a,b), we will add a point (a,b).
        // For queries, we want to count segments satisfying:
        // (a < c and b in (c,d)) or (a in (c,d) and b > d)

        // We'll split queries into two parts and sum results:
        // Part 1: count segments with a < c and b in (c,d)
        // Part 2: count segments with a in (c,d) and b > d

        // To do this efficiently:
        // Sort segments by a ascending.
        // For Part 1:
        // For each query, we want count of segments with a < c and b in (c,d).
        // We can sweep a from smallest to largest, and for each a, add b to Fenwick tree.
        // For each query, when we reach c, we query Fenwick tree for count of b in (c,d).

        // For Part 2:
        // For each query, count segments with a in (c,d) and b > d.
        // We can sweep a from largest to smallest, and for each a, add b to Fenwick tree.
        // For each query, when we reach d, we query Fenwick tree for count of b > d.

        // We'll implement both parts and sum results.

        // Prepare segment arrays for sorting
        int total = M * 2;
        int[] segA = new int[total];
        int[] segB = new int[total];
        for (int i = 0; i < total; i++) {
            segA[i] = segStart[i];
            segB[i] = segEnd[i];
        }

        // Compress segA and segB
        for (int i = 0; i < total; i++) {
            segA[i] = comp.compress(segA[i]);
            segB[i] = comp.compress(segB[i]);
        }

        // Prepare queries for Part 1 and Part 2
        // We'll create events for sweep line

        // Part 1 events: (c, query index, c_comp, d_comp)
        // Part 2 events: (d, query index, c_comp, d_comp)

        // We'll store queries twice (for original and duplicated intervals)
        int totalQ = Q * 2;

        int[] cComp = new int[totalQ];
        int[] dComp = new int[totalQ];
        for (int i = 0; i < totalQ; i++) {
            cComp[i] = comp.compress(qC[i]);
            dComp[i] = comp.compress(qD[i]);
        }

        // Fenwick tree for Part 1 and Part 2
        class Fenwick {
            int n;
            int[] bit;

            Fenwick(int n) {
                this.n = n;
                bit = new int[n + 2];
            }

            void add(int i, int v) {
                while (i <= n) {
                    bit[i] += v;
                    i += i & (-i);
                }
            }

            int sum(int i) {
                int s = 0;
                while (i > 0) {
                    s += bit[i];
                    i -= i & (-i);
                }
                return s;
            }

            int rangeSum(int l, int r) {
                if (r < l) return 0;
                return sum(r) - sum(l - 1);
            }
        }

        Fenwick fenw = new Fenwick(uniqueCount);

        // Part 1: count segments with a < c and b in (c,d)
        // Sort segments by a ascending
        Integer[] segOrder = new Integer[total];
        for (int i = 0; i < total; i++) segOrder[i] = i;
        Arrays.sort(segOrder, (x, y) -> Integer.compare(segA[x], segA[y]));

        // Prepare queries for Part 1: sort by c ascending
        Integer[] qOrder1 = new Integer[totalQ];
        for (int i = 0; i < totalQ; i++) qOrder1[i] = i;
        Arrays.sort(qOrder1, (x, y) -> Integer.compare(cComp[x], cComp[y]));

        int[] ans = new int[Q];

        int segIdx = 0;
        for (int qi : qOrder1) {
            int c_ = cComp[qi];
            int d_ = dComp[qi];
            // Add all segments with a < c_
            while (segIdx < total && segA[segOrder[segIdx]] < c_) {
                fenw.add(segB[segOrder[segIdx]], 1);
                segIdx++;
            }
            // Count segments with b in (c,d) => b > c and b < d
            // So b in (c_, d_-1)
            int count = fenw.rangeSum(c_ + 1, d_ - 1);
            // Add to answer (for original queries only)
            if (qi < Q) ans[qi] += count;
            else ans[qi - Q] += count;
        }

        // Part 2: count segments with a in (c,d) and b > d
        // Sort segments by a descending
        Arrays.sort(segOrder, (x, y) -> Integer.compare(segA[y], segA[x]));

        // Prepare queries for Part 2: sort by d descending
        Integer[] qOrder2 = new Integer[totalQ];
        for (int i = 0; i < totalQ; i++) qOrder2[i] = i;
        Arrays.sort(qOrder2, (x, y) -> Integer.compare(dComp[y], dComp[x]));

        fenw = new Fenwick(uniqueCount);
        segIdx = 0;
        for (int qi : qOrder2) {
            int c_ = cComp[qi];
            int d_ = dComp[qi];
            // Add all segments with a > d_
            while (segIdx < total && segA[segOrder[segIdx]] > d_) {
                fenw.add(segB[segOrder[segIdx]], 1);
                segIdx++;
            }
            // Count segments with a in (c,d) and b > d
            // a in (c_, d_-1), b > d_ => b in (d_, max]
            // We have added segments with a > d_, so now we want to count segments with a in (c_, d_-1)
            // But we only have segments with a > d_ in fenw, so we need to process differently.

            // Instead, we can process queries in order of decreasing d,
            // and for each query, count how many segments with a in (c,d) and b > d.

            // We'll do this by:
            // For each query, total segments with b > d and a > c
            // minus segments with b > d and a >= d+1 (already added)

            // So we need to count segments with a > c and b > d.

            // We'll process segments with a > c and b > d by adding segments with a > c to fenw,
            // but we only added segments with a > d_ so far.

            // To fix this, we process queries in decreasing d order,
            // and for each query, we add segments with a > d_ to fenw,
            // so fenw contains segments with a > d_.

            // Then for query with c_, d_, we want count of segments with a in (c_, d_-1) and b > d_.
            // This equals total segments with a > c_ and b > d_ minus segments with a > d_ and b > d_ (fenw sum).

            // So we need a Fenwick tree that can answer count of segments with a > c_ and b > d_.

            // We'll build another Fenwick tree indexed by a descending order.

            // To simplify, we precompute for all queries the count of segments with a > c_ and b > d_.

            // Let's build a 2D structure is complicated, so we use a trick:

            // We'll process segments sorted by a ascending and build a Fenwick tree on b descending.

            // But this is complex, so we use the following approach:

            // For each query, we can count segments with a > c_ and b > d_ by:
            // total segments - segments with a <= c_ or b <= d_

            // But this is complicated.

            // Instead, we can process Part 2 similarly to Part 1 but swapping roles of a and b.

            // Let's swap a and b in segments and queries and repeat Part 1 logic.

            // So we do Part 2 by swapping a and b in segments and queries and run Part 1 logic again.

        }

        // Implement Part 2 by swapping a and b in segments and queries and repeating Part 1 logic.

        // Swap a and b in segments
        for (int i = 0; i < total; i++) {
            int tmp = segA[i];
            segA[i] = segB[i];
            segB[i] = tmp;
        }

        // Swap c and d in queries
        for (int i = 0; i < totalQ; i++) {
            int tmp = cComp[i];
            cComp[i] = dComp[i];
            dComp[i] = tmp;
        }

        // Sort segments by a ascending (which is original b)
        for (int i = 0; i < total; i++) segOrder[i] = i;
        Arrays.sort(segOrder, (x, y) -> Integer.compare(segA[x], segA[y]));

        // Sort queries by c ascending (which is original d)
        for (int i = 0; i < totalQ; i++) qOrder1[i] = i;
        Arrays.sort(qOrder1, (x, y) -> Integer.compare(cComp[x], cComp[y]));

        fenw = new Fenwick(uniqueCount);
        segIdx = 0;
        for (int qi : qOrder1) {
            int c_ = cComp[qi];
            int d_ = dComp[qi];
            while (segIdx < total && segA[segOrder[segIdx]] < c_) {
                fenw.add(segB[segOrder[segIdx]], 1);
                segIdx++;
            }
            int count = fenw.rangeSum(c_ + 1, d_ - 1);
            if (qi < Q) ans[qi] += count;
            else ans[qi - Q] += count;
        }

        // Output answers for original queries
        for (int i = 0; i < Q; i++) {
            pw.println(ans[i]);
        }

        pw.flush();
        pw.close();
        br.close();
    }
}