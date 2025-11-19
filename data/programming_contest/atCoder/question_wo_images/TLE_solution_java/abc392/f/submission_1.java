import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        FastScanner sc = new FastScanner();
        int N;
        N = sc.nextInt();

        List<Integer> iota = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            iota.add(i);
        }
        TatyamSortedSet set = new TatyamSortedSet(iota);

        int P[] = new int[N];
        for (int i = 0; i < N; i++) {
            P[i] = sc.nextInt() - 1;
        }

        int ans[] = new int[N];
        for (int i = N - 1; i >= 0; i--) {
            ans[set.get(P[i])] = i;
            set.remove(set.get(P[i]));
        }

        for (int i = 0; i < N; i++) {
            System.out.print(ans[i] + 1);
            System.out.print(" ");
        }
        System.out.println();
    }

    public static class TatyamSortedSet {
        final private int BASE_SIZE = 16;
        final private int SPLIT_SIZE = 24;
        private LinkedList<ArrayList<Integer>> list;
        private int size;

        public TatyamSortedSet() {
            list = new LinkedList<>();
            list.add(new ArrayList<>());
            size = 0;
        }

        public TatyamSortedSet(Collection<Integer> collection) {
            ArrayList<Integer> tempList = new ArrayList<>(collection);
            Collections.sort(tempList);
            list = new LinkedList<>();
            size = tempList.size();
            for (int i = 0; i < size; i += BASE_SIZE) {
                list.add(new ArrayList<>(tempList.subList(i, Math.min(i + BASE_SIZE, size))));
            }
        }

        private static class PositionData {
            int listIndex;
            ArrayList<Integer> targetList;
            int innerIndex;

            PositionData(int listIndex, ArrayList<Integer> targetList, int innerIndex) {
                this.listIndex = listIndex;
                this.targetList = targetList;
                this.innerIndex = innerIndex;
            }
        }

        private PositionData position(int x) {

            assert list.size() > 0;
            int idx;
            for (idx = 0; idx < list.size(); idx++) {
                ArrayList<Integer> targetList = list.get(idx);
                if (targetList.size() == 0 || x <= targetList.get(targetList.size() - 1)) {
                    break;
                }
            }
            if (idx == list.size()) {
                idx--;
            }
            assert idx < list.size();

            int innerIndex = 0;
            ArrayList<Integer> targetList = list.get(idx);
            innerIndex = Collections.binarySearch(targetList, x);
            if (innerIndex < 0) {
                innerIndex = -(innerIndex + 1);
            }
            return new PositionData(idx, list.get(idx), innerIndex);
        }

        public boolean contains(int x) {
            PositionData pd = position(x);
            return pd.innerIndex < pd.targetList.size() && pd.targetList.get(pd.innerIndex) == x;
        }

        public boolean add(int x) {
            PositionData pd = position(x);
            if (pd.innerIndex < pd.targetList.size() && pd.targetList.get(pd.innerIndex) == x) {
                return false;
            }
            pd.targetList.add(pd.innerIndex, x);
            size++;
            if (pd.targetList.size() > SPLIT_SIZE) {
                ArrayList<Integer> newList = new ArrayList<>(pd.targetList.subList(BASE_SIZE, pd.targetList.size()));
                pd.targetList.subList(BASE_SIZE, pd.targetList.size()).clear();
                list.add(pd.listIndex + 1, newList);
            }
            return true;
        }

        public boolean remove(int x) {
            PositionData pd = position(x);
            if (pd.innerIndex == pd.targetList.size() || pd.targetList.get(pd.innerIndex) != x) {
                return false;
            }
            pd.targetList.remove(pd.innerIndex);
            size--;
            if (pd.targetList.size() == 0 && list.size() > 1) {
                list.remove(pd.listIndex);
            }
            return true;
        }

        public int size() {
            return size;
        }

        public boolean isEmpty() {
            return size == 0;
        }

        public int get(int index) {
            assert 0 <= index && index < size;
            int idx = index;
            for (ArrayList<Integer> targetList : list) {
                if (idx < targetList.size()) {
                    return targetList.get(idx);
                } else {
                    idx -= targetList.size();
                }
            }
            throw new IndexOutOfBoundsException();
        }

        public String toString() {
            StringBuilder sb = new StringBuilder();
            sb.append("{");
            boolean first = true;
            for (ArrayList<Integer> targetList : list) {
                for (int x : targetList) {
                    if (!first) {
                        sb.append(", ");
                    }
                    sb.append(x);
                    first = false;
                }
            }
            sb.append("}");
            return sb.toString();
        }
    }

    public static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }

        public String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }

}