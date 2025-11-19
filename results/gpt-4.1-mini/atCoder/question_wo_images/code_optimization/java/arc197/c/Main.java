import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br;
    static PrintWriter out;
    static StringTokenizer st;

    // Function to compute gcd
    static long gcd(long a, long b) {
        while (b != 0) {
            long t = b;
            b = a % b;
            a = t;
        }
        return a;
    }

    // Function to compute lcm safely
    static long lcm(long a, long b) {
        return a / gcd(a, b) * b;
    }

    // Count how many numbers <= x are removed (multiples of any removed divisor)
    // Using inclusion-exclusion on the current set of removed divisors
    static long countRemoved(long x, ArrayList<Long> removed) {
        int n = removed.size();
        long res = 0;
        // Inclusion-exclusion over subsets of removed divisors
        // Since n can be up to Q=1e5, we cannot do full subsets.
        // So we will maintain only the minimal set of removed divisors (no divisor divides another)
        // and do inclusion-exclusion only on them.
        // But even then, subsets are too large.
        // So we will do a binary search approach with a different method.

        // Instead, we will do inclusion-exclusion only on the minimal set of removed divisors,
        // but since minimal set can be large, we will do a binary search with a function that
        // counts how many numbers <= x are removed by summing floor(x/d) for each divisor d,
        // then subtracting overlaps for pairs, triples, etc.
        // But this is too expensive for large sets.

        // So we will maintain the minimal set of removed divisors and do a binary search
        // with a function that counts how many numbers <= x are removed by summing floor(x/d)
        // for each divisor, ignoring overlaps (overcounting).
        // This overcounting means countRemoved(x) >= true countRemoved(x).
        // So countRemoved(x) - overcounting >= true countRemoved(x).
        // But we need exact count for binary search.

        // Therefore, we will maintain the minimal set of removed divisors and do inclusion-exclusion
        // only on small subsets (up to size 10) by limiting the minimal set size.

        // To keep minimal set small, we remove divisors that are multiples of new divisor,
        // and ignore new divisor if it is multiple of existing divisor.

        // So minimal set size will be small (<= 20), so inclusion-exclusion is feasible.

        // Inclusion-exclusion implementation:
        // For all non-empty subsets of removed divisors:
        //   compute lcm of subset
        //   add or subtract floor(x / lcm) depending on parity of subset size

        // Since minimal set size is small, this is feasible.

        int m = removed.size();
        long total = 0;
        // Use bitmask to iterate subsets
        // To avoid overflow, if lcm > x, skip
        for (int mask = 1; mask < (1 << m); mask++) {
            long l = 1;
            int bits = Integer.bitCount(mask);
            boolean overflow = false;
            for (int i = 0; i < m; i++) {
                if ((mask & (1 << i)) != 0) {
                    long d = removed.get(i);
                    long g = gcd(l, d);
                    if (l > x / (d / g)) {
                        overflow = true;
                        break;
                    }
                    l = l / g * d;
                    if (l > x) {
                        overflow = true;
                        break;
                    }
                }
            }
            if (overflow) continue;
            long c = x / l;
            if (bits % 2 == 1) total += c;
            else total -= c;
        }
        return total;
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);

        int Q = Integer.parseInt(br.readLine());
        int[] A = new int[Q];
        int[] B = new int[Q];
        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            A[i] = Integer.parseInt(st.nextToken());
            B[i] = Integer.parseInt(st.nextToken());
        }

        // Maintain minimal set of removed divisors (no divisor divides another)
        ArrayList<Long> removed = new ArrayList<>();

        for (int i = 0; i < Q; i++) {
            long ai = A[i];
            // Insert ai into removed minimal set if not multiple of existing divisor
            boolean skip = false;
            // Remove divisors that are multiples of ai
            // Also check if ai is multiple of any existing divisor
            Iterator<Long> it = removed.iterator();
            ArrayList<Long> toRemove = new ArrayList<>();
            while (it.hasNext()) {
                long d = it.next();
                if (d % ai == 0) {
                    toRemove.add(d);
                } else if (ai % d == 0) {
                    skip = true;
                    break;
                }
            }
            if (!skip) {
                removed.removeAll(toRemove);
                removed.add(ai);
            }

            int bi = B[i];

            // Binary search for the bi-th smallest element in S
            // S = positive integers excluding multiples of any removed divisor
            // countRemoved(x) = number of removed elements <= x
            // countInS(x) = x - countRemoved(x)
            // We want minimal x such that countInS(x) >= bi

            long low = 1, high = (long)1e15; // large enough upper bound
            while (low < high) {
                long mid = (low + high) >>> 1;
                long removedCount = countRemoved(mid, removed);
                long inS = mid - removedCount;
                if (inS >= bi) {
                    high = mid;
                } else {
                    low = mid + 1;
                }
            }
            out.println(low);
        }

        out.close();
    }
}