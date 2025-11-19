import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        int[] a = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        int[][] queries = new int[q][2];
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            queries[i][0] = Integer.parseInt(st.nextToken()) - 1; // R_i - 1 for 0-indexing
            queries[i][1] = Integer.parseInt(st.nextToken());
        }

        // To store answers
        int[] answers = new int[q];
        // To process the queries
        List<Query> queryList = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            queryList.add(new Query(queries[i][0], queries[i][1], i));
        }
        Collections.sort(queryList, (a1, a2) -> Integer.compare(a1.r, a2.r));

        // To maintain the lengths of the longest increasing subsequences seen so far
        TreeMap<Integer, Integer> dp = new TreeMap<>();
        int listIndex = 0;

        for (Query query : queryList) {
            while (listIndex <= query.r) {
                int num = a[listIndex];
                // Find maximum length for num
                Integer length = dp.floorKey(num);
                if (length == null) {
                    dp.put(num, 1);
                } else {
                    int newLength = dp.get(length) + 1;
                    // Update our DP table
                    if (!dp.containsKey(num)) {
                        dp.put(num, newLength);
                    } else {
                        dp.put(num, Math.max(dp.get(num), newLength));
                    }
                }
                listIndex++;
            }
            // Answer for the current query
            Integer maxLength = dp.floorEntry(query.x) == null ? 0 : dp.floorEntry(query.x).getValue();
            answers[query.index] = maxLength;
        }

        for (int answer : answers) {
            pw.println(answer);
        }

        pw.close();
    }

    static class Query {
        int r, x, index;

        Query(int r, int x, int index) {
            this.r = r;
            this.x = x;
            this.index = index;
        }
    }
}