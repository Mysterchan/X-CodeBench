import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // Use BufferedReader and BufferedWriter for fast IO
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        // We will process each test case independently
        // The key insight:
        // The maximum number of black cells painted is:
        // (H * W) - (number of cells never visited by any path)
        // The cells never visited are those that cannot be reached by any path X satisfying the constraints.
        //
        // For each position i in S (0-based), we know S[i] in {D, R, ?}
        // The path X must have exactly H-1 Ds and W-1 Rs.
        // For each i:
        // - If S[i] == 'D', then X[i] == 'D'
        // - If S[i] == 'R', then X[i] == 'R'
        // - If S[i] == '?', then X[i] can be either 'D' or 'R'
        //
        // We want to find the union of all cells visited by all valid X.
        //
        // The problem reduces to:
        // For each step i (0 to H+W-3), the possible moves at that step are:
        // - If S[i] == 'D', only down
        // - If S[i] == 'R', only right
        // - If S[i] == '?', both down and right possible
        //
        // So the set of possible positions after i steps is the union of all paths choosing allowed moves.
        //
        // We want to find the total number of distinct cells visited by any such path.
        //
        // Approach:
        // We can simulate the possible positions reachable at each step using two arrays:
        // - minD[i]: minimum number of down moves used up to step i
        // - maxD[i]: maximum number of down moves used up to step i
        //
        // Similarly for right moves:
        // - minR[i] = i - maxD[i]
        // - maxR[i] = i - minD[i]
        //
        // Because at each step:
        // - If S[i] == 'D', down moves increase by 1
        // - If S[i] == 'R', right moves increase by 1
        // - If S[i] == '?', down or right moves can increase by 1
        //
        // So minD[i] and maxD[i] can be computed iteratively.
        //
        // After processing all steps, the set of reachable cells is all (d+1, r+1) where d in [minD[i], maxD[i]] and r = i - d.
        //
        // The union of all these intervals over i = 0 to H+W-2 covers a certain area.
        //
        // The total number of black cells painted is the size of this union.
        //
        // We can compute the union of intervals of d for each i, then sum over all i the number of distinct cells.
        //
        // But this is complicated.
        //
        // Instead, we use a known formula from editorial:
        //
        // The answer = H * W - (number of cells never visited)
        //
        // The cells never visited are those that cannot be reached by any path X.
        //
        // The cells never visited are those that lie outside the union of all possible paths.
        //
        // The union of all possible paths is the set of cells (h,w) such that:
        // - The number of down moves used to reach (h,w) is d = h-1
        // - The number of right moves used is r = w-1
        // - There exists a path X consistent with S that has d down moves and r right moves at the corresponding steps.
        //
        // We can find the minimal and maximal number of down moves at each step i.
        //
        // Then the minimal number of down moves at step i is minD[i]
        // The maximal number of down moves at step i is maxD[i]
        //
        // For each cell (h,w), the step index is i = (h-1)+(w-1) = h + w - 2
        //
        // The cell (h,w) is reachable if and only if:
        // minD[i] <= h-1 <= maxD[i]
        //
        // So the total number of reachable cells is sum over i=0 to H+W-2 of (maxD[i] - minD[i] + 1)
        //
        // But we must consider the grid boundaries:
        // h in [1,H], w in [1,W]
        //
        // So for each i, h-1 in [max(0, i-(W-1)), min(H-1, i)]
        //
        // So the intersection of [minD[i], maxD[i]] and [max(0, i-(W-1)), min(H-1, i)] gives the reachable down moves at step i.
        //
        // The count of reachable cells at step i is:
        // max(0, min(maxD[i], min(H-1, i)) - max(minD[i], max(0, i-(W-1))) + 1)
        //
        // Summing over i gives the total number of reachable cells.
        //
        // This is O(H+W) per test case, which is efficient enough.

        for (int _ = 0; _ < T; _++) {
            String[] hw = br.readLine().split(" ");
            int H = Integer.parseInt(hw[0]);
            int W = Integer.parseInt(hw[1]);
            String S = br.readLine();

            int n = H + W - 2;
            char[] s = S.toCharArray();

            // minD[i]: minimal number of down moves after i steps
            // maxD[i]: maximal number of down moves after i steps
            int[] minD = new int[n + 1];
            int[] maxD = new int[n + 1];

            minD[0] = 0;
            maxD[0] = 0;

            for (int i = 0; i < n; i++) {
                char c = s[i];
                if (c == 'D') {
                    minD[i + 1] = minD[i] + 1;
                    maxD[i + 1] = maxD[i] + 1;
                } else if (c == 'R') {
                    minD[i + 1] = minD[i];
                    maxD[i + 1] = maxD[i];
                } else { // '?'
                    minD[i + 1] = minD[i];
                    maxD[i + 1] = maxD[i] + 1;
                }
            }

            long result = 0;
            for (int i = 0; i <= n; i++) {
                // step i corresponds to cells where h-1 + w-1 = i
                // h-1 in [max(0, i-(W-1)), min(H-1, i)]
                int lowH = Math.max(0, i - (W - 1));
                int highH = Math.min(H - 1, i);

                // intersection with [minD[i], maxD[i]]
                int low = Math.max(minD[i], lowH);
                int high = Math.min(maxD[i], highH);

                if (high >= low) {
                    result += (high - low + 1);
                }
            }

            sb.append(result).append('\n');
        }

        System.out.print(sb);
    }
}