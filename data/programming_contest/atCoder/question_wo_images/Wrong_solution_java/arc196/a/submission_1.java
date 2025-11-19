import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        Queue<int[]> q = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                int diff1 = Math.abs(arr[o1[0]] - arr[o1[1]]);
                int diff2 = Math.abs(arr[o2[0]] - arr[o2[1]]);

                return diff2 - diff1;
            }
        });

        arr[0] = sc.nextInt();

        for(int i = 1; i < n; i++) {
            arr[i] = sc.nextInt();
            q.add(new int[]{i - 1, i});
        }

        boolean[] vis = new boolean[n];
        long ans = 0;

        while (!q.isEmpty()) {
            int[] brr = q.remove();

            if(vis[brr[0]] || vis[brr[1]]) {
                continue;
            }

            vis[brr[0]] = true;
            vis[brr[1]] = true;
            ans += Math.abs(arr[brr[0]] - arr[brr[1]]);

            if(brr[0] > 0 && brr[1] < n - 1) {
                q.add(new int[]{brr[0] - 1, brr[1] + 1});
            }
        }

        System.out.println(ans);

    }

}