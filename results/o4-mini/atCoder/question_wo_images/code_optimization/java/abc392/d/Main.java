import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long[] K = new long[N];
        List<Map<Integer,Integer>> maps = new ArrayList<>(N);
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int ki = Integer.parseInt(st.nextToken());
            K[i] = ki;
            Map<Integer,Integer> map = new HashMap<>();
            for (int j = 0; j < ki; j++) {
                int v = Integer.parseInt(st.nextToken());
                map.put(v, map.getOrDefault(v, 0) + 1);
            }
            maps.add(map);
        }

        double maxProb = 0.0;
        for (int i = 0; i < N; i++) {
            Map<Integer,Integer> mi = maps.get(i);
            for (int j = i + 1; j < N; j++) {
                Map<Integer,Integer> mj = maps.get(j);
                Map<Integer,Integer> small = mi.size() <= mj.size() ? mi : mj;
                Map<Integer,Integer> big = mi.size() <= mj.size() ? mj : mi;
                long same = 0;
                for (Map.Entry<Integer,Integer> e : small.entrySet()) {
                    Integer cnt2 = big.get(e.getKey());
                    if (cnt2 != null) {
                        same += (long)e.getValue() * cnt2;
                    }
                }
                if (same > 0) {
                    double denom = (double)K[i] * K[j];
                    double prob = same / denom;
                    if (prob > maxProb) {
                        maxProb = prob;
                    }
                }
            }
        }

        System.out.printf("%.15f\n", maxProb);
    }
}