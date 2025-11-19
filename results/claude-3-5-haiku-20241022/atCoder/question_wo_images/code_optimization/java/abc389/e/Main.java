import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br;
    static PrintWriter out;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);
        new Main().solve();
        out.flush();
    }

    public void solve() throws IOException {
        String[] line1 = br.readLine().split(" ");
        int n = Integer.parseInt(line1[0]);
        long m = Long.parseLong(line1[1]);
        
        String[] line2 = br.readLine().split(" ");
        long[] p = new long[n];
        long minp = Long.MAX_VALUE;
        for(int i = 0; i < n; i++) {
            p[i] = Long.parseLong(line2[i]);
            minp = Math.min(minp, p[i]);
        }

        long l = 0;
        long r = (long)(Math.sqrt((double)m / minp) + 1);
        
        while(r - l > 1) {
            long mid = (l + r) / 2;
            long sump = 0;
            boolean overflow = false;
            
            for(int i = 0; i < n; i++) {
                long k = (mid / p[i] + 1) / 2;
                long cost = p[i] * k * k;
                if(sump > m - cost) {
                    overflow = true;
                    break;
                }
                sump += cost;
            }
            
            if(overflow || sump > m) {
                r = mid;
            } else {
                l = mid;
            }
        }

        long res = 0;
        long[] k = new long[n];
        for(int i = 0; i < n; i++) {
            k[i] = (l / p[i] + 1) / 2;
            res += k[i];
            m -= p[i] * k[i] * k[i];
        }

        PriorityQueue<Item> pq = new PriorityQueue<>();
        for(int i = 0; i < n; i++) {
            long nextCost = (2 * k[i] + 1) * p[i];
            if(nextCost <= m) {
                pq.add(new Item(p[i], k[i] + 1, nextCost));
            }
        }

        while(!pq.isEmpty()) {
            Item it = pq.poll();
            if(m >= it.price) {
                m -= it.price;
                res++;
                long nextCost = (2 * it.k + 1) * it.base;
                if(nextCost <= m) {
                    pq.add(new Item(it.base, it.k + 1, nextCost));
                }
            } else {
                break;
            }
        }
        
        out.println(res);
    }

    static class Item implements Comparable<Item> {
        long base;
        long k;
        long price;
        
        Item(long base, long k, long price) {
            this.base = base;
            this.k = k;
            this.price = price;
        }

        public int compareTo(Item other) {
            return Long.compare(this.price, other.price);
        }
    }
}