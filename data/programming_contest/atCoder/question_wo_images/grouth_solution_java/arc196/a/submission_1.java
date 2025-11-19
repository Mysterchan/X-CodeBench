import java.io.*;
import java.util.*;

public class Main {

    static int[] medianSlidingWindow(int[] nums, int k) {
        DualHeap dh = new DualHeap();
        for (int i = 0; i < k; ++i) {
            dh.insert(nums[i]);
        }
        int[] ans = new int[nums.length - k + 1];
        op = new long[nums.length - k + 1];
        ans[0] = dh.getMedian();
        op[0] = (long) ans[0] * dh.smallSize - dh.smallSum + dh.largeSum - (long) ans[0] * dh.largeSize;
        for (int i = k; i < nums.length; ++i) {
            dh.insert(nums[i]);
            dh.erase(nums[i - k]);
            ans[i - k + 1] = dh.getMedian();
            op[i - k + 1] = dh.getDiff();
        }
        return ans;
    }

    static class DualHeap {

        private PriorityQueue<Integer> small;

        private PriorityQueue<Integer> large;

        private Map<Integer, Integer> delayed;

        long smallSum, largeSum;

        private int smallSize, largeSize;

        public DualHeap() {
            this.small = new PriorityQueue<Integer>(new Comparator<Integer>() {
                public int compare(Integer num1, Integer num2) {
                    return num2.compareTo(num1);
                }
            });
            this.large = new PriorityQueue<Integer>(new Comparator<Integer>() {
                public int compare(Integer num1, Integer num2) {
                    return num1.compareTo(num2);
                }
            });
            this.delayed = new HashMap<Integer, Integer>();
            this.smallSize = 0;
            this.largeSize = 0;
            this.smallSum = 0;
            this.largeSum = 0;
        }

        public int getMedian() {
            assert !small.isEmpty();
            return small.peek();

        }

        public void insert(int num) {
            if (small.isEmpty() || num <= small.peek()) {
                small.offer(num);
                smallSum += num;
                ++smallSize;
            } else {
                large.offer(num);
                largeSum += num;
                ++largeSize;
            }
            makeBalance();
        }

        public void erase(int num) {
            delayed.put(num, delayed.getOrDefault(num, 0) + 1);

            if (num <= small.peek()) {
                --smallSize;
                smallSum -= num;
                if (num == small.peek()) {
                    prune(small, 0);
                }
            } else {
                --largeSize;
                largeSum -= num;
                if (num == large.peek()) {
                    prune(large, 1);
                }
            }
            makeBalance();
        }

        private void prune(PriorityQueue<Integer> heap, int t) {
            while (!heap.isEmpty()) {
                int num = heap.peek();
                if (delayed.containsKey(num)) {
                    delayed.put(num, delayed.get(num) - 1);
                    if (delayed.get(num) == 0) {
                        delayed.remove(num);
                    }
                    int d = heap.poll();

                } else {
                    break;
                }
            }
        }

        private void makeBalance() {
            if (smallSize > largeSize + 1) {

                int d = small.poll();
                smallSum -= d;
                largeSum += d;
                large.offer(d);
                --smallSize;
                ++largeSize;

                prune(small, 0);
            } else if (smallSize < largeSize) {

                int d = large.poll();
                largeSum -= d;
                smallSum += d;
                small.offer(d);
                ++smallSize;
                --largeSize;

                prune(large, 1);
            }
        }

        public long getDiff() {
            int mid = getMedian();
            return (long) mid * smallSize - smallSum + largeSum - (long) mid * largeSize;
        }

    }

    static long[] op;

    public static void main(String[] args) {
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        if (n % 2 == 0) {
            Arrays.sort(a);
            long ans = 0;
            for (int i = 0, j = n - 1; i <= j; i++, j--) {
                ans += a[j] - a[i];
            }
            out.println(ans);
        } else {
            int len = (n + 1) / 2;
            long[] b = new long[len];
            int j = 1;
            DualHeap dh = new DualHeap();
            for (int i = 1; i < n; i += 2) {
                dh.insert(a[i]);
                dh.insert(a[i - 1]);
                b[j] = dh.largeSum - dh.smallSum;
                j++;
            }
            j = len - 2;
            dh = new DualHeap();
            for (int i = n - 2; i >= 0; i -= 2) {
                dh.insert(a[i]);
                dh.insert(a[i + 1]);
                b[j] += dh.largeSum - dh.smallSum;
                j--;
            }
            long ans = 0;
            for (int i = 0; i < len; i++) {
                ans = Math.max(ans, b[i]);
            }
            out.println(ans);

        }
        out.close();
    }

    static Kattio sc = new Kattio();
    static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    static class Kattio {
        static BufferedReader r;
        static StringTokenizer st;

        public Kattio() {
            r = new BufferedReader(new InputStreamReader(System.in));
        }

        public String next() {
            try {
                while (st == null || !st.hasMoreTokens()) {
                    st = new StringTokenizer(r.readLine());
                }
                return st.nextToken();
            } catch (Exception e) {
                return null;
            }
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }
    }
}