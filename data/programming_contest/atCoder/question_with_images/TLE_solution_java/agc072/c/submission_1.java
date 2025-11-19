    import java.util.*;
    import java.io.*;
    public class Main {
        static class FastReader {
            BufferedReader br;
            StringTokenizer st;
            public FastReader() {
                br = new BufferedReader(new InputStreamReader(System.in));
            }
            String next() {
                while (st == null || !st.hasMoreElements()) {
                    try {
                        st = new StringTokenizer(br.readLine());
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
                return st.nextToken();
            }
            int nextInt() {
                return Integer.parseInt(next());
            }
            long nextLong() {
                return Long.parseLong(next());
            }
            double nextDouble() {
                return Double.parseDouble(next());
            }
            String nextLine() {
                String str = "";
                try {
                    str = br.readLine();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                return str;
            }
        }
        static void sort(int a[]){
            ArrayList<Integer> arr=new ArrayList<>();
            for(int i=0;i<a.length;i++)
                arr.add(a[i]);
            Collections.sort(arr);
            for(int i=0;i<a.length;i++)
                a[i]=arr.get(i);
        }

        static long lcm(int a, int b)
        {
            return (a / gcd(a, b)) * b;
        }

        private static long gcd(long a, long b)
        {
            if (b == 0) {
                return a;
            }
            return gcd(b, a % b);
        }

        static long modInverse(long n, long p)
        {
            return power(n, p - 2, p);
        }

        static long nCrModPFermat(int n, int r, long p)
        {
            if (r == 0)
                return 1;

            long[] fac = new long[n + 1];
            fac[0] = 1;

            for (int i = 1; i <= n; i++)
                fac[i] = fac[i - 1] * i % p;

            return (fac[n] * modInverse(fac[r], p) % p
                    * modInverse(fac[n - r], p) % p)
                    % p;
        }
        static long power(long x, long y, long p)
        {

            long res = 1;

            x = x % p;

            while (y > 0) {

                if (y % 2 == 1)
                    res = (res * x) % p;

                y = y >> 1;
                x = (x * x) % p;
            }

            return res;
        }
        static int log(long n){
            if(n<=1)return 0;
            long temp = n;
            int res = 0;
            while(n>1){
                res++;
                n/=2;
            }
            return (1l<<res)==temp?res:res+1;
        }

        static class Pair<A, B> {
            A first;
            B second;

            public Pair(A first, B second)
            {
                this.first = first;
                this.second = second;
            }
        }

        static int[] readIntArray(int n) {
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            return arr;
        }
        static long[] readLongArray(int n) {
            long[] arr = new long[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextLong();
            }
            return arr;
        }
        static long[][] readLong2DArray(int rows, int cols) {
            long[][] arr = new long[rows][cols];
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    arr[i][j] = sc.nextLong();
                }
            }
            return arr;
        }

        static int[][] readInt2DArray(int rows, int cols) {
            int[][] arr = new int[rows][cols];
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    arr[i][j] = sc.nextInt();
                }
            }
            return arr;
        }

        static void bfs(List<List<Integer>> adj, int start) {
            boolean[] visited = new boolean[adj.size()];
            Queue<Integer> queue = new LinkedList<>();

            queue.add(start);
            visited[start] = true;

            while (!queue.isEmpty()) {
                int node = queue.poll();

                System.out.print(node + " ");

                for (int neighbor : adj.get(node)) {
                    if (!visited[neighbor]) {
                        visited[neighbor] = true;
                        queue.add(neighbor);
                    }
                }
            }
        }

        static void dfs(List<List<Integer>> adj, boolean[] visited, int node) {
            visited[node] = true;

            System.out.print(node + " ");

            for (int neighbor : adj.get(node)) {
                if (!visited[neighbor]) {
                    dfs(adj, visited, neighbor);
                }
            }
        }

        static int mod = (int)1e9+7;
        static int INF = Integer.MAX_VALUE;
        static PrintWriter out;
        static FastReader sc ;

        public static void main(String[] args) throws IOException {
            sc = new FastReader();
            out = new PrintWriter(System.out);

            solveC();
            out.flush();
        }
        public static void solveC() {
            int n = sc.nextInt();
            long k = sc.nextLong();
            long[][] arr = new long[n][n];

            for(int i = 0; i < k - 1; i++) {
                move(arr, 0, 0);
            }

            StringBuilder str = new StringBuilder();
            int i = 0, j = 0;

            while(i < n -1 && j < n -1){
                if(i + 1 < n && j + 1 < n && arr[i + 1][j] <= arr[i][j + 1]) {
                    i++;
                    str.append('D');
                }else if(i + 1 < n && j + 1 < n && arr[i + 1][j] > arr[i][j + 1]) {
                    j++;
                    str.append('R');
                }else if(i + 1 < n) {
                    str.append('D');
                }else str.append('R');
            }

            while(i < n - 1) {
                str.append('D');
                i++;
            }
            while(j < n - 1) {
                str.append('R');
                j++;
            }
            System.out.println(str.toString());

        }
        public static void move(long[][] arr, int i, int j) {
            if(i == arr.length - 1 && j == arr.length - 1) return;
            arr[i][j]++;
            int n = arr.length;
            if(i + 1 < n && j + 1 < n && arr[i + 1][j] > arr[i][j + 1]) {
                move(arr, i, j + 1);
            }else if(i + 1 < n && j + 1 < n && arr[i + 1][j] <= arr[i][j + 1]) {
                move(arr, i + 1, j);
            }else if(i + 1 < n) {
                move(arr, i +1 , j);
            }else {
                move(arr, i, j + 1);
            }
        }
        public static void solveA() {
            int n = sc.nextInt();
            long d = sc.nextLong();

            PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
            for(int i = 0; i < n; i++) {
                long t = sc.nextLong();
                long x = sc.nextLong();
                pq.offer(new long[]{t, x});
            }

            long currTime = 0;

            while(!pq.isEmpty()) {
                long[] curr = pq.poll();

                currTime += curr[1];

                if(currTime < curr[0]) {
                    currTime = curr[0];
                }
                if(currTime > curr[0] + d) {
                    System.out.println("No");
                    return;
                }

                currTime += curr[1];

            }
            System.out.println("Yes");
        }
    }