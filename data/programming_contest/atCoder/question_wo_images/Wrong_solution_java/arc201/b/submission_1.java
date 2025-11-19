import java.util.*;

public class Main {
    static class Node implements Comparable<Node> {
        int w;
        long val;

        public Node(int w, long val) {
            this.w = w;
            this.val = val;
        }

        @Override
        public int compareTo(Node other) {
            if (this.w != other.w) {
                return Integer.compare(other.w, this.w);
            }
            return Long.compare(this.val, other.val);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        while (t-- > 0) {
            long n = scanner.nextLong();
            long w = scanner.nextLong();

            PriorityQueue<Node> q = new PriorityQueue<>();

            for (int i = 0; i < n; i++) {
                int weight = scanner.nextInt();
                long value = scanner.nextLong();
                q.add(new Node(weight, value));
            }

            long ans = 0;

            for (int i = 0; i <= 60; i++) {
                if ((w & (1L << i)) != 0 && !q.isEmpty() && q.peek().w <= i) {
                    ans += q.peek().val;
                    q.poll();
                }

                while (q.size() >= 2 && !q.isEmpty() && q.peek().w <= i) {
                    Node u = q.poll();
                    if (q.isEmpty()) {
                        q.add(u);
                        break;
                    }
                    Node v = q.poll();

                    if (u.w == v.w) {
                        q.add(new Node(u.w + 1, u.val + v.val));
                    } else {
                        q.add(new Node(u.w + 1, u.val));
                        q.add(v);
                    }
                }
            }

            System.out.println(ans);
        }

        scanner.close();
    }
}