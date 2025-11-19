import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        int n = sc.nextInt();
        int[] a = new int[n], b = new int[n];
        
        List<Integer> aVals = new ArrayList<>();
        List<Integer> bVals = new ArrayList<>();
        int aWild = 0, bWild = 0;
        
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
            if (a[i] == -1) aWild++;
            else aVals.add(a[i]);
        }
        for (int i = 0; i < n; i++) {
            b[i] = sc.nextInt();
            if (b[i] == -1) bWild++;
            else bVals.add(b[i]);
        }
        
        // If all are wildcards or if we have enough wildcards
        if (aWild + bWild >= n) {
            out.println("Yes");
            out.close();
            return;
        }
        
        // Try all possible sums
        Set<Integer> possibleSums = new HashSet<>();
        for (int av : aVals) {
            for (int bv : bVals) {
                possibleSums.add(av + bv);
            }
        }
        
        for (int sum : possibleSums) {
            // Count how many can be satisfied
            int satisfied = 0;
            
            // Match non-wild A with non-wild B
            boolean[] usedA = new boolean[aVals.size()];
            boolean[] usedB = new boolean[bVals.size()];
            
            for (int i = 0; i < aVals.size(); i++) {
                for (int j = 0; j < bVals.size(); j++) {
                    if (!usedA[i] && !usedB[j] && aVals.get(i) + bVals.get(j) == sum) {
                        usedA[i] = true;
                        usedB[j] = true;
                        satisfied++;
                        break;
                    }
                }
            }
            
            // Count remaining non-wild values that can pair with wildcards
            int remainA = 0, remainB = 0;
            for (int i = 0; i < aVals.size(); i++) {
                if (!usedA[i] && aVals.get(i) <= sum) remainA++;
            }
            for (int j = 0; j < bVals.size(); j++) {
                if (!usedB[j] && bVals.get(j) <= sum) remainB++;
            }
            
            // Can we satisfy with wildcards?
            satisfied += Math.min(remainA, bWild);
            satisfied += Math.min(remainB, aWild);
            satisfied += Math.max(0, aWild + bWild - remainA - remainB);
            
            if (satisfied >= n) {
                out.println("Yes");
                out.close();
                return;
            }
        }
        
        out.println("No");
        out.close();
    }

    static Kattio sc = new Kattio();
    static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    static class Kattio {
        static BufferedReader r;
        static StringTokenizer st;

        public Kattio() {
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
}