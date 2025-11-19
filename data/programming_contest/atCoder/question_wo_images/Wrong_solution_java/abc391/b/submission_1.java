import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    String[] s = new String[n];
    String[] t = new String[m];

    for (int i = 0; i < n; i++)
      s[i] = br.readLine();

    for (int i = 0; i < m; i++)
      t[i] = br.readLine();

    boolean ok = true;
    for (int i = 0; i < n - m + 1; i++) {
      for (int j = 0; j < n - m + 1; j++) {
        ok = true;
        if (s[i].charAt(j) == t[0].charAt(0)) {

          for (int a = 0; a < m; a++) {
            for (int b = 0; b < m; b++) {

              if (s[i + a].charAt(j + b) != t[a].charAt(b)) {
                ok = false;
                break;
              }
            }
            if (!ok)
              break;
          }

        }
        if (ok) {
          System.out.println((i + 1) + " " + (j + 1));
          return;
        }
      }
    }

  }
}