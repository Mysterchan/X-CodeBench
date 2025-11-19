import java.util.*;

public class Main {
    static final int MOD = 998244353;
    static int N;
    static int[] A;
    static List<Integer> unknowns;
    static long[][] dp;
    static boolean[][] computed;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        A = new int[N];
        unknowns = new ArrayList<>();
        
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
            if (A[i] == -1) {
                unknowns.add(i);
            }
        }

        if (unknowns.isEmpty()) {
            System.out.println(isGoodSequence() ? 1 : 0);
            return;
        }

        System.out.println(solve(0));
    }

    static long solve(int pos) {
        if (pos == unknowns.size()) {
            return isGoodSequence() ? 1 : 0;
        }

        long result = 0;
        int idx = unknowns.get(pos);

        for (int val = 1; val <= N; val++) {
            A[idx] = val;
            if (isValidSoFar(pos)) {
                result = (result + solve(pos + 1)) % MOD;
            }
        }

        A[idx] = -1;
        return result;
    }

    static boolean isValidSoFar(int pos) {
        // Early pruning: check intervals that are now fully determined
        return true;
    }

    static boolean isGoodSequence() {
        for (int l = 1; l <= N; l++) {
            for (int r = l; r <= N; r++) {
                if (!hasValidX(l, r)) {
                    return false;
                }
            }
        }
        return true;
    }

    static boolean hasValidX(int l, int r) {
        for (int x = l; x <= r; x++) {
            if (formsTree(l, r, x)) {
                return true;
            }
        }
        return false;
    }

    static boolean formsTree(int l, int r, int skip) {
        int size = r - l + 1;
        int[] parent = new int[N + 1];
        for (int i = 0; i <= N; i++) parent[i] = i;
        
        int edgeCount = 0;
        
        for (int i = l; i <= r; i++) {
            if (i != skip) {
                int target = A[i - 1];
                if (target < l || target > r) return false;
                if (i == target) return false;
                
                int pi = find(parent, i);
                int pt = find(parent, target);
                if (pi == pt) return false;
                parent[pi] = pt;
                edgeCount++;
            }
        }
        
        return edgeCount == size - 1;
    }

    static int find(int[] parent, int x) {
        if (parent[x] != x) {
            parent[x] = find(parent, parent[x]);
        }
        return parent[x];
    }
}