import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;

public class Main {

    static long countBadSubarrays(List<Integer> positions, int N) {
        long count = 0;
        int lastPos = -1;

        for (int p : positions) {

            long len = p - lastPos - 1;
            count += len * (len + 1) / 2;
            lastPos = p;
        }

        long len = N - lastPos - 1;
        count += len * (len + 1) / 2;

        return count;
    }

    static List<Integer> merge(List<Integer> list1, List<Integer> list2) {
        List<Integer> merged = new ArrayList<>(list1.size() + list2.size());
        int i = 0, j = 0;
        while (i < list1.size() && j < list2.size()) {
            if (list1.get(i) < list2.get(j)) {
                merged.add(list1.get(i++));
            } else {
                merged.add(list2.get(j++));
            }
        }
        while (i < list1.size()) merged.add(list1.get(i++));
        while (j < list2.size()) merged.add(list2.get(j++));
        return merged;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        int N = Integer.parseInt(br.readLine());
        int[] A = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());

        List<Integer>[] pos = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) {
            pos[i] = new ArrayList<>();
        }

        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
            pos[A[i]].add(i);
        }

        long[] C_v_c = new long[N + 1];
        C_v_c[0] = (long)N * (N + 1) / 2;
        for (int v = 1; v <= N; v++) {
            C_v_c[v] = countBadSubarrays(pos[v], N);
        }

        long totalSum = 0;
        for (int v = 1; v <= N; v++) {

            long C_v_minus_1_c = C_v_c[v - 1];

            List<Integer> mergedList = merge(pos[v], pos[v - 1]);
            long C_merged_c = countBadSubarrays(mergedList, N);

            long g_v = C_v_minus_1_c - C_merged_c;
            totalSum += g_v;
        }

        out.println(totalSum);
        out.flush();
    }
}