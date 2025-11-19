import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String s = br.readLine();
    int targetSize = 3;
    int searchCnt = 0;

    for (int i = 0; i < s.length() - targetSize; i++) {
      if (s.charAt(i) == 'A') {
        for (int j = 1; i < s.length() - j * 2; j++) {
          if (s.charAt(i + j) == 'B' && s.charAt(i + j * 2) == 'C') {
            searchCnt++;
          }
        }
      }
    }
    System.out.println(searchCnt);
  }
}