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
                return Integer.compare(this.w, other.w);
            }
            return Long.compare(other.val, this.val);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        while (t-- > 0) {
            long n = scanner.nextLong();
            long w = scanner.nextLong();

            PriorityQueue<Node> queue = new PriorityQueue<>();

            for (int i = 0; i < n; i++) {
                int weight = scanner.nextInt();
                long value = scanner.nextLong();
                queue.offer(new Node(weight, value));
            }

            long ans = 0;

            for (int i = 0; i <= 60; i++) {
                if ((w & (1L << i)) != 0 && !queue.isEmpty() && queue.peek().w <= i) {
                    ans += queue.poll().val;
                }

                while (queue.size() >= 2 && !queue.isEmpty() && queue.peek().w <= i) {
                    Node u = queue.poll();
                    Node v = queue.poll();

                    if (u.w == v.w) {
                        queue.offer(new Node(u.w + 1, u.val + v.val));
                    } else {
                        queue.offer(new Node(u.w + 1, u.val));
                        queue.offer(v);
                    }
                }
            }

            System.out.println(ans);
        }

        scanner.close();
    }
}