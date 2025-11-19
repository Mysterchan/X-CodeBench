import java.io.*;
import java.util.*;

public class Main {

    static Scanner sc;
    static PrintWriter out;

    public static void main(String[] args) {
        sc = new Scanner(System.in);
        out = new PrintWriter(System.out);
        new Main().solve();
        out.flush();
    }

    public void solve() {

        int n = sc.nextInt();
        long m = sc.nextLong();
        PriorityQueue<Item> pq = new PriorityQueue<>((a,b) -> Long.compare(a.price, b.price));
        long[] p = new long[n];
        long minp = Long.MAX_VALUE;
        for(int i=0;i<n;i++) {
            p[i] = sc.nextLong();
            minp = Math.min(minp, p[i]);
        }

        long l = 0;
        long r = (long)(Math.sqrt(1d * m / minp) + 1);
        A: while(r-l>1) {
            long mid = (l+r)/2;
            long sump = 0;
            for(int i=0;i<n;i++) {
                long k = (mid/p[i] + 1)/2;
                sump += p[i] * k * k;
                if(sump > m) {
                    r = mid;
                    continue A;
                }
            }
            l = mid;
        }

        long res = 0;
        for(int i=0;i<n;i++) {
            long k = (l/p[i] + 1)/2;
            res += k;
            pq.add(new Item(p[i], (int)k+1));
            m -= p[i] * k * k;
        }

        while(m>0 && !pq.isEmpty()) {
            Item it = pq.poll();
            if (m >= it.price) {
                m -= it.price;
                res++;
                pq.add(it.next());
            } else {
                break;
            }
        }
        out.println(res);
    }

    static class Item {
        long base;
        int k;
        long price;
        Item(long base, int k) {
            this.base = base;
            this.k = k;
            this.price = (2L * k - 1) * base;
        }
        Item next() {
            return new Item(base, k+1);
        }

    }
}