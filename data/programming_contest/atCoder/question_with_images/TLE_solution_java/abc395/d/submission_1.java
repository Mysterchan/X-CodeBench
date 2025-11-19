import java.util.*;

class Main {

  static Scanner sc = new Scanner(System.in);

  public static void main(String[] args) {
    int N = ni();
    int[] P = new int[N + 1];
    for (int i = 1; i <= N; i++) {
      P[i] = i;
    }
    Map<Integer, Set<Integer>> pmap = new HashMap<>();
    for (int i = 1; i <= N; i++) {
      Set<Integer> set = new HashSet<>();
      set.add(i);
      pmap.put(i, set);
    }
    int Q = ni();
    while (Q-- > 0) {
      int q = ni();
      if (q == 1) {
        int a = ni();
        int b = ni();
        pmap.get(P[a]).remove(a);
        pmap.get(b).add(a);
        P[a] = b;
      } else if (q == 2) {
        int a = ni();
        int b = ni();
        Set<Integer> setA = pmap.get(a);
        Set<Integer> setB = pmap.get(b);
        pmap.put(a, setB);
        pmap.put(b, setA);
        for (int x : setA) {
          P[x] = b;
        }
        for (int x : setB) {
          P[x] = a;
        }
      } else if (q == 3) {
        int a = ni();
        System.out.println(P[a]);
      }
    }

    sc.close();
  }

  static int ni() {
    return sc.nextInt();
  }

  static long nl() {
    return sc.nextLong();
  }

  static String nn() {
    return sc.next();
  }

  static char nc() {
    return sc.next().charAt(0);
  }
}