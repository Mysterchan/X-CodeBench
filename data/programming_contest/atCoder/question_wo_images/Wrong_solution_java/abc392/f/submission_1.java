import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) {
    MyScanner sc = new MyScanner();
    out = new PrintWriter(new BufferedOutputStream(System.out));

    int n = sc.nextInt();
    int m = n;

    StringBuilder sb = new StringBuilder();
    char num = '0';

    while (m-- > 0) {
      num++;
      int idx = sc.nextInt();

      if (sb.length() >= idx) {
        sb.insert(idx - 1, num);
      } else {
        sb.append(num);
      }

    }

    for (char elem : sb.toString().toCharArray()) {
      System.out.print(elem + " ");
    }

    out.close();
  }

  public static PrintWriter out;

  public static class MyScanner {
    BufferedReader br;
    StringTokenizer st;

    public MyScanner() {
      br = new BufferedReader(new InputStreamReader(System.in));
    }

    String next() {
      while (st == null || !st.hasMoreElements()) {
        try {
          st = new StringTokenizer(br.readLine());
        } catch (IOException e) {
          e.printStackTrace();
        }
      }
      return st.nextToken();
    }

    int nextInt() {
      return Integer.parseInt(next());
    }

    long nextLong() {
      return Long.parseLong(next());
    }

    double nextDouble() {
      return Double.parseDouble(next());
    }

    String nextLine() {
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