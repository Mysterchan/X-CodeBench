import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] weights = new int[n+1];

        for(int i=1;i<=n;i++){
            weights[i] = sc.nextInt();
        }

        List<int[]> pairs = new ArrayList<>();

        for (int i=0;i<n;i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            pairs.add(new int[]{a,b});
        }

        List<List<Integer>> adj = new ArrayList<>();
        for(int i=0;i<=n;i++){
            adj.add(new ArrayList<>());
        }

        for(int i=0;i<n;i++){
            int[] p1 = pairs.get(i);

            for(int j=i+1;j<n;j++){
                int[] p2 = pairs.get(j);
                boolean intExists = intersect(p1,p2);

                if(!intExists){
                    adj.get(i+1).add(j+1);
                    adj.get(j+1).add(i+1);
                }
            }
        }

        int q = sc.nextInt();

        for(int i=0;i<q;i++){
            int s = sc.nextInt();
            int t = sc.nextInt();

            System.out.println(dijkstra(adj,s,t,n,weights));
        }
    }

    public static boolean intersect(int[] p1, int[] p2) {
        int a1 = p1[0];
        int a2 = p1[1];
        int b1 = p2[0];
        int b2 = p2[1];
        return !(a2 < b1 || b2 < a1);
    }

    public static long dijkstra(List<List<Integer>> adj, int start, int end, int n, int[] weights){
        long[] dist = new long[n+1];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[start] = weights[start];
        
        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[1], b[1]));
        pq.offer(new long[]{start, weights[start]});
        
        while(!pq.isEmpty()){
            long[] curr = pq.poll();
            int node = (int)curr[0];
            long currDist = curr[1];
            
            if(node == end){
                return currDist;
            }
            
            if(currDist > dist[node]){
                continue;
            }
            
            for(int neighbor : adj.get(node)){
                long newDist = currDist + weights[neighbor];
                if(newDist < dist[neighbor]){
                    dist[neighbor] = newDist;
                    pq.offer(new long[]{neighbor, newDist});
                }
            }
        }
        
        return -1;
    }
}