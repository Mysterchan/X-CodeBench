import java.io.*;
import java.util.*;

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

    static PrintWriter out = new PrintWriter(System.out);
    static FastReader fr = new FastReader();

    public static void main(String[] args) {
        int t = fr.nextInt();
        while (t-- > 0) {
            solve();
        }
        out.flush();
    }
    static class ValueComparator implements Comparator<Map.Entry<?, Integer>> {
        @Override
        public int compare(Map.Entry<?, Integer> e1, Map.Entry<?, Integer> e2) {
            return Integer.compare(e1.getValue(), e2.getValue());
        }
    }
    static void solve() {
        int n = fr.nextInt();
        int k = fr.nextInt();

        Map<Integer,Integer> mp = new HashMap<>();
        int max = Integer.MIN_VALUE;
        for(int i=0;i<n;i++){
            int a = fr.nextInt();
            max = Math.max(max, a);
            mp.put((i+1), a);
        }
        if(max == mp.get(k)){
            System.out.println("YES");
        }
        else {
            boolean flag = false;
            List<Map.Entry<Integer, Integer>> list = new ArrayList<>(mp.entrySet());
            list.sort(new ValueComparator());

            int cnt = 0;
            int prev = 0;
            for(Map.Entry<Integer,Integer> e : list){

                if(cnt>0){
                    if(prev < (e.getValue()-prev)){
                        flag = true;
                        break;
                    }
                    else{
                        prev = e.getValue();
                    }
                }
                if(e.getKey()==k && cnt==0){
                    prev = e.getValue();
                    cnt++;
                }
            }

            if(flag){
                System.out.println("NO");
            }
            else{
                System.out.println("YES");
            }

        }
    }

    static void sort(int[] arr) {
        Arrays.sort(arr);
    }

    static long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    static long lcm(long a, long b) {
        return (a / gcd(a, b)) * b;
    }

    static long modPow(long a, long e) {
        long res = 1;
        while (e > 0) {
            if ((e & 1) == 1) res = (res * a);
            a = (a * a);
            e >>= 1;
        }
        return res;
    }

    public static boolean isSorted(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                return false;
            }
        }
        return true; 
    }


    public static boolean isPrime(int n) {
        if (n < 2) return false;
        if (n == 2 || n == 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}
