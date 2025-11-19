import java.util.*;

class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    final long L = sc.nextLong();
    final long R = sc.nextLong();
    long total = 0;

    for (long i = L; i <= R; i++) {
      String s = String.valueOf(i);
      char[] c = s.toCharArray();
      boolean ok = true;

      for (int j = 1; j < c.length; j++) {
        if (c[0] <= c[j]) {
          ok = false;
          break;
        }
      }

      if (ok) {
        total++;
      }
    }

    System.out.println(total);
  }
}