import java.io.*;
import java.util.*;

public class Main {
    static class MyScanner {
        static BufferedReader r;
        static StringTokenizer st;
        public MyScanner() {
            r = new BufferedReader(new InputStreamReader(System.in));
        }
        public String next() {
            try {
                while (st == null || !st.hasMoreTokens()) {
                    st = new StringTokenizer(r.readLine());
                }
                return st.nextToken();
            } catch (Exception e) {
                return null;
            }
        }
        public int nextInt() {
            return Integer.parseInt(next());
        }
    }
    
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static MyScanner sc = new MyScanner();
    static int N;
    static int[] a;
    
    public static void main(String[] args) throws IOException {
        N = sc.nextInt();
        int length = (int) Math.pow(3, N);
        a = new int[length];
        String input = sc.next();
        
        for (int i = 0; i < length; i++) {
            a[i] = input.charAt(i) - '0';
        }
        
        int finalValue = getFinalValue(0, length - 1, N);
        int changesToZero = countChanges(0, length - 1, N, 0);
        int changesToOne = countChanges(0, length - 1, N, 1);
        
        int result = finalValue == 0 ? changesToOne : changesToZero;
        bw.write(result + "");
        bw.flush();
    }

    private static int getFinalValue(int l, int r, int n) {
        if (l == r) return a[l];
        int oneCount = 0, zeroCount = 0;
        int groupSize = (int) Math.pow(3, n - 1);
        
        for (int i = l; i <= r; i += groupSize) {
            int majority = getMajority(i, i + groupSize - 1);
            if (majority == 1) oneCount++;
            else zeroCount++;
        }
        
        return oneCount >= zeroCount ? 1 : 0;
    }

    private static int getMajority(int l, int r) {
        int count0 = 0, count1 = 0;
        for (int i = l; i <= r; i++) {
            if (a[i] == 0) count0++;
            else count1++;
        }
        return count1 > count0 ? 1 : 0;
    }

    private static int countChanges(int l, int r, int n, int target) {
        if (l == r) return a[l] == target ? 0 : 1;
        int changes = 0;
        int groupSize = (int) Math.pow(3, n - 1);
        
        for (int i = l; i <= r; i += groupSize) {
            int majority = getMajority(i, i + groupSize - 1);
            if (majority == target) continue;
            changes += groupSize - Math.max(countInGroup(i, i + groupSize - 1, 0), countInGroup(i, i + groupSize - 1, 1));
        }
        
        return changes;
    }

    private static int countInGroup(int l, int r, int value) {
        int count = 0;
        for (int i = l; i <= r; i++) {
            if (a[i] == value) count++;
        }
        return count;
    }
}