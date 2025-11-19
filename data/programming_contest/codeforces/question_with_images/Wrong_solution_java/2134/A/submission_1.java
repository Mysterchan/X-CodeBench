import java.sql.ClientInfoStatus;
import java.util.*;
import java.io.*;
import  static  java.lang.Math.*;

public class Main {

    static class Pair{

        int first;
        int second;

        public Pair(int first, int second) {
            this.first = first;
            this.second = second;
        }

        @Override
        public String toString() {
            return "{"+first+","+second+"}";
        }
    }

    static class Tuple{

        int first;
        int second;
        int third;
        public Tuple(int first, int second,int third) {
            this.first = first;
            this.second = second;
            this.third=third;
        }
    }

    static  FastWriter out = new FastWriter();

    static FastScanner in=new FastScanner();

    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner(String s) {
            try {
                br = new BufferedReader(new FileReader(s));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        public FastScanner() {
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
    }


    public static class FastWriter {
        private final BufferedWriter bw;

        public FastWriter() {
            this.bw = new BufferedWriter(new OutputStreamWriter(System.out));
        }

        public void print(Object object) throws IOException {
            bw.append( object+" ");
        }

        public void println(Object object) throws IOException {
            print(object);
            bw.append("\n");
        }

        public void close() throws IOException {
            bw.close();
        }
    }

    static boolean[] sieve(int n){

        boolean[] isPrime=new boolean[n+1];
        Arrays.fill(isPrime,true);
        isPrime[0]=false;
        isPrime[1]=false;

        for(int i=2;i*i<=n;i++){
            if(isPrime[i]){
                for(int j=i*i;j<=n;j+=i) isPrime[j]=false;
            }
        }

        return isPrime;
    }

    static List<Integer> PrimeFactors(int num) {

        List<Integer> ans = new ArrayList<>();
        while (num % 2 == 0) {
            ans.add(2);
            num /= 2;
        }
        for (int i = 3; i <= Math.sqrt(num); i++) {
            while (num % i == 0) {
                ans.add(i);
                num /= i;
            }
        }
        if (num > 2) ans.add(num);
        return ans;
    }

    static List<Integer> getFactors(int n) {
        List<Integer> factors = new ArrayList<>();
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                factors.add(i);
                if (i != n / i) factors.add(n / i);
            }
        }
        return factors;
    }


    static public int upper_bound(int[] array,int key,int start){

        int lowerBound = start;
        while (lowerBound < array.length) {
            if (key >= array[lowerBound])
                lowerBound++;
            else
                return lowerBound;
        }

        return lowerBound;
    }

    static   public int lower_bound(int[] array,int key,int start){

        int lowerBound = start;
        while (lowerBound < array.length) {
            if (key > array[lowerBound])
                lowerBound++;
            else
                return lowerBound;
        }

        return lowerBound;
    }

    static long gcd(long a, long b) {

        if (b == 0)
            return a;
        else
            return gcd(b, a % b);
    }

    static long lcm(long a, long b) {
        return Math.abs(a * b) / gcd(a,b);
    }

    static public  long power(long A, long B, long C) {
        if (A == 0)
            return 0;
        if (B == 0)
            return 1;
        long y;
        if (B % 2 == 0) {
            y = power(A, B / 2, C);
            y = (y * y) % C;
        }
        // If B is odd
        else {
            y = A % C;
            y = (y * power(A, B - 1, C) % C) % C;
        }
        return ((y + C) % C);
    }

    static void sort(int[] arr){

        List<Integer> list=new ArrayList<>();

        for(int it:arr) list.add(it);

        Collections.sort(list);

        for(int i=0;i<list.size();i++) arr[i]=list.get(i);
    }

    static void reverse(int[] arr){
        int low=0,high=arr.length-1;
        while(low<high){
            int val=arr[low];
            arr[low]=arr[high];
            arr[high]=val;
            low++;high--;
        }
    }


    public static String sortString(String inputString)
    {
        char tempArray[] = inputString.toCharArray();
        Arrays.sort(tempArray);
        return new String(tempArray);
    }

    public  static int[] inputArray(int n){

        int[] arr=new int[n];
        for(int i=0;i<arr.length;i++) arr[i]=in.nextInt();

        return arr;
    }

    public  static long[] inputArrayLong(int m){

        long[] arr=new long[m];
        for(int i=0;i<arr.length;i++) arr[i]=in.nextLong();

        return arr;
    }

    public static int[][] inputArray(int m,int n){

        int[][] arr=new int[m][n];
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr[0].length;j++) arr[i][j]=in.nextInt();
        }

        return arr;
    }

    public static long[][] inputArrayLong(int m,int n){

        long[][] arr=new long[m][n];
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr[0].length;j++) arr[i][j]=in.nextLong();
        }

        return arr;
    }



    private static boolean isPrime(long n) {

        if(n<=1) return false;

        for(int i=2;i<=Math.sqrt(n);i++){
            if(n%i==0) return false;
        }
        return true;
    }

    static long mod=(long)1e9+7;

    static int[] dir={0,1,0,-1,0};

    static int x[] = { -1, -1, -1,  0, 0,  1, 1, 1 };
    static int y[] = { -1,  0,  1, -1, 1, -1, 0, 1 };

    public static int calculateManhattanDistance(int x1, int y1, int x2, int y2) {
        return Math.abs(x1 - x2) + Math.abs(y1 - y2);
    }
    static int[][] moves = {
            {-2, -1}, {-1, -2}, {1, -2}, {2, -1},
            {-2, 1}, {-1, 2}, {1, 2}, {2, 1}
    };

    public static void main(String[] args) {
        try {
            int  testCases = in.nextInt();
            int t=0;
            while(t++ <testCases){
                rajdhakar062003(testCases,t);
            }
            out.close();
        } catch (Exception e) {
            return;
        }
    }

   static Integer[][] dp;

    static List<List<Integer>> edge;

    private static void rajdhakar062003(int testcase,int t) throws IOException {

        int n=in.nextInt(),a=in.nextInt(),b=in.nextInt();

        if(a<b){
            if((b%2==0 && n%2==0) || (b%2!=0 && a%2!=0)) out.println("YES");
            else out.println("NO");
        }
        else{
            if((a%2==0 && b%2==0) || (a%2!=0 && b%2!=0)) out.println("YES");
            else out.println("NO");
        }

    }
}
