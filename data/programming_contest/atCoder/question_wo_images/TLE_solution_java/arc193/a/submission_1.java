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

            System.out.println(bfs(adj,s,t,weights[s],new boolean[n+1],weights));
        }

    }

public static boolean intersect(int[] p1, int[] p2) {
    int a1 = p1[0];
    int a2 = p1[1];
    int b1 = p2[0];
    int b2 = p2[1];
    return !(Math.max(a1, a2) < Math.min(b1, b2) || Math.max(b1, b2) < Math.min(a1, a2));
}

    public static int bfs(List<List<Integer>> adj, int i, int j, int w, boolean[] visited,int[] weights){

        Queue<int[]> pq = new LinkedList<>();
        pq.add(new int[]{i,w});

        while(!pq.isEmpty()){

            int[] node =pq.poll();

            i = node[0];
            w = node[1];

            if(j == i){
                return w;
            }

            visited[i] = true;
            List<Integer> nei = adj.get(i);

            for(int n:nei){
                if(!visited[n]){
                    pq.add(new int[]{n,w+weights[n]});
                }
            }

        }
        return -1;
    }
}