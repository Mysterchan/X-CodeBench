        import java.io.*;
        import java.lang.reflect.Array;
        import java.util.*;
        import static java.lang.Math.*;

        public class Main {
            static int count = 0;

            static class SegmentTree {
                int size;
                long[] maxArr;
                long[] sumArr;

                public SegmentTree(int n) {
                    size = 1;
                    while (size < n) size *= 2;
                    maxArr = new long[2 * size];
                    sumArr = new long[2 * size];
                    Arrays.fill(maxArr, Long.MIN_VALUE);
                    Arrays.fill(sumArr, 0);
                }

                public void set(int i, int v, int x, int lx, int rx) {
                    if (rx - lx == 1) {
                        maxArr[x] = v;
                        sumArr[x] = v;
                        return;
                    }
                    int m = (lx + rx) / 2;
                    if (i < m) {
                        set(i, v, 2 * x + 1, lx, m);
                    } else {
                        set(i, v, 2 * x + 2, m, rx);
                    }
                    maxArr[x] = Math.max(maxArr[2 * x + 1], maxArr[2 * x + 2]);
                    sumArr[x] = sumArr[2 * x + 1] + sumArr[2 * x + 2];
                }

                public void set(int i, int v) {
                    set(i, v, 0, 0, size);
                }

                public long max(int l, int r, int x, int lx, int rx) {
                    if (lx >= r || l >= rx) return Long.MIN_VALUE;
                    if (lx >= l && rx <= r) return maxArr[x];
                    int m = (lx + rx) / 2;
                    long m1 = max(l, r, 2 * x + 1, lx, m);
                    long m2 = max(l, r, 2 * x + 2, m, rx);
                    return Math.max(m1, m2);
                }

                public long max(int l, int r) {
                    return max(l, r, 0, 0, size);
                }

                public long sum(int l, int r, int x, int lx, int rx) {
                    if (lx >= r || l >= rx) return 0;
                    if (lx >= l && rx <= r) return sumArr[x];
                    int m = (lx + rx) / 2;
                    long s1 = sum(l, r, 2 * x + 1, lx, m);
                    long s2 = sum(l, r, 2 * x + 2, m, rx);
                    return s1 + s2;
                }

                public long sum(int l, int r) {
                    return sum(l, r, 0, 0, size);
                }

                public void build(int[] a, int x, int lx, int rx) {
                    if (rx - lx == 1) {
                        if (lx < a.length) {
                            maxArr[x] = a[lx];
                            sumArr[x] = a[lx];
                        }
                        return;
                    }
                    int m = (lx + rx) / 2;
                    build(a, 2 * x + 1, lx, m);
                    build(a, 2 * x + 2, m, rx);
                    maxArr[x] = Math.max(maxArr[2 * x + 1], maxArr[2 * x + 2]);
                    sumArr[x] = sumArr[2 * x + 1] + sumArr[2 * x + 2];
                }

                public void build(int[] a) {
                    build(a, 0, 0, size);
                }
            }

            static final int MOD = 1_000_000_007;
            static final int INF = Integer.MAX_VALUE;
            static final long LINF = Long.MAX_VALUE;
            static FastReader in = new FastReader();
            static PrintWriter out = new PrintWriter(System.out);

            public static void main(String[] args) throws IOException {
                int t = 1;
                while (t-- > 0) {
                    solve();
                }
                out.flush();
            }

            static int fact(int n) {
                if (n == 0) return 1;
                return n * fact(n - 1);
            }

            static void solve() {
                int n = in.nextInt();
                int[] arr = readIntArray(n);

                Map<String, Integer> memo = new HashMap<>();
                Stack<Integer> st = new Stack<>();

                int best = dfs(0, st, 0, arr, memo);
                out.println(best);
            }

            public static int dfs(int i, Stack<Integer> st, int sum, int[] arr, Map<String, Integer> memo) {
                if (i == arr.length) return sum;

                String key = i + "|" + sum + "|" + st.toString();
                if (memo.containsKey(key)) return memo.get(key);

                st.push(arr[i]);
                int take = dfs(i + 1, st, sum + arr[i], arr, memo);
                st.pop();

                int rem = Integer.MIN_VALUE;
                if (!st.isEmpty()) {
                    int top = st.pop();
                    rem = dfs(i + 1, st, sum - top, arr, memo);
                    st.push(top);
                }

                int res = Math.max(take, rem);
                memo.put(key, res);
                return res;
            }

            static int digitSum(int num) {
                int sum = 0;
                while (num > 0) {
                    sum += num % 10;
                    num /= 10;
                }
                return sum;
            }

            static boolean isPrime(int n){
                if(n <= 1){
                    return false;
                }
                for(int i = 2; i <= sqrt(n); i++){
                    if(n%i == 0){
                        return false;
                    }
                }
                return true;
            }

            public void reverse(int[] arr, int start, int end){

                int left = start;
                int right = end;

                while(left < right){
                    int temp = arr[left];
                    arr[left] = arr[right];
                    arr[right] = arr[left];
                    left++;
                    right--;
                }
            }

            static int popcount(int x){
                int cnt = 0;

                int mask = 1;

                int BITS = 30;
                for(int i = 0; i <= BITS; i++){
                    if((x & mask<<i) != 0) cnt++;
                }
                return cnt;
            }

            static boolean parity(int x){
                if(popcount(x) %2 == 1) return true;
                return false;
            }

            static int lowbit(int x){
                int saved = -1;

                int BIT = 32;
                for(int i = BIT; i >= 0; i--){
                    if((x & (1 << i)) != 0) saved=i;
                }
                return saved;
            }

            public static int mex(List<Integer> a) {
                int mex = 0;
                Set<Integer> set = new HashSet<>();
                for (int n : a) set.add(n);
                while (set.contains(mex)) mex++;
                return mex;
            }

            static Set<Integer> getMissing(int[] arr, int max) {
                Set<Integer> set = new HashSet<>();
                Set<Integer> miss = new HashSet<>();
                for (int n : arr) set.add(n);
                for (int i = 1; i <= max; i++) {
                    if (!set.contains(i)) miss.add(i);
                }
                return miss;
            }

            public static boolean isSubsequence(String a, String b) {
                int i = 0;
                for (int j = 0; j < b.length(); j++) {
                    if (i < a.length() && a.charAt(i) == b.charAt(j)) i++;
                }
                return i == a.length();
            }

            public static boolean isValid(int r, int c, int aR, int aC) {
                if (r == aR || c == aC) return false;
                return abs(r - aR) != abs(c - aC);
            }

            static long gcd(long a, long b) {
                return b == 0 ? a : gcd(b, a % b);
            }

            static long lcm(long a, long b) {
                return a / gcd(a, b) * b;
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
                long nextLong() { return Long.parseLong(next()); }
                double nextDouble() { return Double.parseDouble(next()); }
                String nextLine() {
                    String str = "";
                    try { str = br.readLine(); }
                    catch (IOException e) { e.printStackTrace(); }
                    return str;
                }
            }

            static int[] readIntArray(int n) {
                int[] a = new int[n];
                for (int i = 0; i < n; i++) a[i] = in.nextInt();
                return a;
            }

            static void printArray(int[] a) {
                for (int val : a) out.print(val + " ");
                out.println();
            }

            static long binExp(long base, long exp, long mod) {
                long result = 1;
                base %= mod;
                while (exp > 0) {
                    if ((exp & 1) == 1) {
                        result = (result * base) % mod;
                    }
                    base = (base * base) % mod;
                    exp >>= 1;
                }
                return result;
            }
        }