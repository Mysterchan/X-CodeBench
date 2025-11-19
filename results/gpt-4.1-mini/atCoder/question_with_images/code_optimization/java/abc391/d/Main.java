import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // Use BufferedReader and BufferedWriter for faster IO
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());

        // For each column, store the Y coordinates of blocks in a sorted array
        // Also store the block indices in the same order
        ArrayList<Integer>[] ys = new ArrayList[W + 1];
        ArrayList<Integer>[] ids = new ArrayList[W + 1];
        for (int i = 1; i <= W; i++) {
            ys[i] = new ArrayList<>();
            ids[i] = new ArrayList<>();
        }

        // To answer queries, we need to know for each block:
        // - its column x
        // - its index in the column (to find its "layer")
        // We'll store these in arrays indexed by block id (1-based)
        int[] xOf = new int[N + 1];
        int[] yOf = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            xOf[i] = x;
            yOf[i] = y;
            ys[x].add(y);
            ids[x].add(i);
        }

        // Sort each column by Y ascending
        for (int i = 1; i <= W; i++) {
            ArrayList<Integer> yList = ys[i];
            ArrayList<Integer> idList = ids[i];
            // Sort by y using a custom comparator on pairs
            int size = yList.size();
            Integer[] idx = new Integer[size];
            for (int j = 0; j < size; j++) idx[j] = j;
            Arrays.sort(idx, (a, b) -> Integer.compare(yList.get(a), yList.get(b)));

            ArrayList<Integer> sortedY = new ArrayList<>(size);
            ArrayList<Integer> sortedId = new ArrayList<>(size);
            for (int j = 0; j < size; j++) {
                sortedY.add(yList.get(idx[j]));
                sortedId.add(idList.get(idx[j]));
            }
            ys[i] = sortedY;
            ids[i] = sortedId;
        }

        // The key insight:
        // The blocks in each column form a stack.
        // The bottom-most block in the column is at index 0 in ys[i].
        // The "layer" of a block is its index in the sorted ys[i].
        // The number of full rows removed up to time T is min(T, total full rows).
        // A full row is removed when all columns have a block at that row.
        // The number of full rows removed is limited by the minimal height of columns.

        // Compute the minimal height among columns
        int minHeight = Integer.MAX_VALUE;
        for (int i = 1; i <= W; i++) {
            minHeight = Math.min(minHeight, ys[i].size());
        }

        // For each block, find its layer (index in its column)
        // We'll store layerOf[block_id] = layer (0-based)
        int[] layerOf = new int[N + 1];
        for (int i = 1; i <= W; i++) {
            ArrayList<Integer> idList = ids[i];
            for (int j = 0; j < idList.size(); j++) {
                layerOf[idList.get(j)] = j;
            }
        }

        // Number of queries
        int Q = Integer.parseInt(br.readLine());

        // For each query:
        // block exists at time T+0.5 if and only if:
        // layerOf[block] >= number of full rows removed at time T
        // number of full rows removed at time T = min(T, minHeight)
        // Because after minHeight full rows removed, no more full rows can be removed.

        for (int q = 0; q < Q; q++) {
            st = new StringTokenizer(br.readLine());
            int T = Integer.parseInt(st.nextToken());
            int A = Integer.parseInt(st.nextToken());

            int removedRows = T < minHeight ? T : minHeight;
            if (layerOf[A] >= removedRows) {
                bw.write("Yes\n");
            } else {
                bw.write("No\n");
            }
        }
        bw.flush();
    }
}