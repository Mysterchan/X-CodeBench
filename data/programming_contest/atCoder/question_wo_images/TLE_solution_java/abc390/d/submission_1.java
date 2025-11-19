import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class Main {
    public static class Pair{
        int src;
        int dst;
        Pair(int src, int dst) {
            this.src = src;
            this.dst = dst;
        }
        @Override
        public String toString() {
            return String.format("src, dst: (%d, %d)", this.src, this.dst);
        }
    }

    public static long get_xor(long [] arr) {
        long ret = arr[0];
        for (int i = 1; i < arr.length; i++) {
            ret = ret ^ arr[i];
        }
        return ret;
    }

    public static void get_number_of_solutions(long [] arr, Set<Long> solution_set) {
        solution_set.add(get_xor(arr));
        ArrayList<Pair> merge_indices = get_merge_indices(arr);
        for (int i = 0; i < merge_indices.size(); i++) {
            Pair cur_pair = merge_indices.get(i);
            long prev_src_val = arr[cur_pair.src];

            arr[cur_pair.dst] += prev_src_val;
            arr[cur_pair.src] = 0;
            get_number_of_solutions(arr, solution_set);

            arr[cur_pair.dst] -= prev_src_val;
            arr[cur_pair.src] = prev_src_val;
        }
    }

    public static ArrayList<Pair> get_merge_indices(long [] arr) {
        ArrayList<Pair> index_pairs = new ArrayList<Pair>();
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] != (long) 0 && arr[j] != (long) 0) {
                    index_pairs.add(new Pair(i, j));
                }
            }
        }
        return index_pairs;
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        long [] arr = new long[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }
        Set<Long> solution_set = new HashSet<Long>();
        get_number_of_solutions(arr, solution_set);
        pw.println(solution_set.size());
        pw.close();
    }
}