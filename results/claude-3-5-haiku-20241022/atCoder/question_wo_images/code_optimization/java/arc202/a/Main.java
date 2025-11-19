import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.PriorityQueue;

public class Main {
    static class Node implements Comparable<Node> {
        int val, count, id;
        Node prev, next;
        boolean removed;

        public Node(int val, int count, int id) {
            this.val = val;
            this.count = count;
            this.id = id;
            this.removed = false;
        }

        public int compareTo(Node o) {
            if (this.val != o.val) return Integer.compare(this.val, o.val);
            return Integer.compare(this.id, o.id);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int tt = Integer.parseInt(br.readLine());
        
        for (int t = 0; t < tt; t++) {
            int n = Integer.parseInt(br.readLine());
            String[] tokens = br.readLine().split(" ");
            
            Node head = new Node(Integer.parseInt(tokens[0]), 1, 0);
            Node prev = head;
            int idx = 1;
            
            for (int i = 1; i < n; i++) {
                int val = Integer.parseInt(tokens[i]);
                if (val == prev.val) {
                    prev.count++;
                } else {
                    Node curr = new Node(val, 1, idx++);
                    prev.next = curr;
                    curr.prev = prev;
                    prev = curr;
                }
            }
            
            PriorityQueue<Node> pq = new PriorityQueue<>();
            Node node = head;
            while (node != null) {
                pq.offer(node);
                node = node.next;
            }
            
            long ans = 0;
            
            while (!pq.isEmpty()) {
                Node curr = pq.poll();
                
                if (curr.removed) continue;
                
                if (pq.isEmpty() && curr.count == 1) break;
                
                int cost = curr.count % 2;
                ans += cost;
                int newVal = curr.val + 1;
                int newCount = (curr.count + cost) / 2;
                
                Node left = curr.prev;
                Node right = curr.next;
                
                if (left != null && left.val == newVal) {
                    left.removed = true;
                    newCount += left.count;
                    curr.prev = left.prev;
                    if (left.prev != null) left.prev.next = curr;
                }
                
                if (right != null && right.val == newVal) {
                    right.removed = true;
                    newCount += right.count;
                    curr.next = right.next;
                    if (right.next != null) right.next.prev = curr;
                }
                
                curr.val = newVal;
                curr.count = newCount;
                pq.offer(curr);
            }
            
            sb.append(ans).append('\n');
        }
        
        System.out.print(sb);
    }
}