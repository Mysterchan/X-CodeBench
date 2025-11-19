import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.TreeSet;

public class Main {
    static class Node {
        int val, count, id;
        Node prev, next;

        public Node(int val, int count, int id) {
            this.val = val;
            this.count = count;
            this.id = id;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader bu = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String[] s = bu.readLine().split(" ");
        int tt = Integer.parseInt(s[0]);
        for (int t = 0; t < tt; t++) {
            s = bu.readLine().split(" ");
            int n = Integer.parseInt(s[0]);
            int[] a = new int[n];
            s = bu.readLine().split(" ");
            for (int i = 0; i < n; i++) a[i] = Integer.parseInt(s[i]);
            ArrayList<Node> al = new ArrayList<>();
            int cur = a[0], curCount = 1;
            for (int i = 1; i < n; i++) {
                if (a[i] == cur) curCount++;
                else {
                    al.add(new Node(cur, curCount, i));
                    cur = a[i];
                    curCount = 1;
                }
            }
            al.add(new Node(cur, curCount, n));
            TreeSet<Node> ts = new TreeSet<>(Comparator.<Node>comparingInt(o -> o.val).thenComparingInt(o -> o.id));
            Node head = al.get(0);
            ts.add(head);
            Node prevNode = head;
            for (int i = 1; i < al.size(); i++) {
                Node curNode = al.get(i);
                curNode.prev = prevNode;
                prevNode.next = curNode;
                ts.add(curNode);
                prevNode = curNode;
            }
            long ans = 0;
            while (!ts.isEmpty()) {
                Node curNode = ts.first();
                assert curNode != null;
                if (ts.size() == 1 && curNode.count == 1) break;
                int cost = curNode.count % 2;
                ans += cost;
                int newVal = curNode.val + 1, newCount = (curNode.count + cost) / 2;
                ts.pollFirst();

                Node leftNode = curNode.prev, rightNode = curNode.next;
                if (leftNode != null && leftNode.val == newVal) {
                    ts.remove(leftNode);
                    newCount += leftNode.count;
                    if (leftNode.prev != null) leftNode.prev.next = curNode;
                    curNode.prev = leftNode.prev;
                }
                if (rightNode != null && rightNode.val == newVal) {
                    ts.remove(rightNode);
                    newCount += rightNode.count;
                    if (rightNode.next != null) rightNode.next.prev = curNode;
                    curNode.next = rightNode.next;
                }
                curNode.val = newVal;
                curNode.count = newCount;
                ts.add(curNode);
            }

            sb.append(ans + "\n");
        }
        System.out.print(sb);
    }
}