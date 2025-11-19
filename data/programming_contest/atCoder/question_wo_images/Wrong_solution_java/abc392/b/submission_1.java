import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    st = new StringTokenizer(br.readLine());

    List<Integer> numbers = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      numbers.add(i + 1);
    }
    List<Integer> a = new ArrayList<>();
    for (int i = 0; i < m; i++) {
      a.add(Integer.parseInt(st.nextToken()));
    }

    for (int i = 0; i < m; i++) {
      int number = a.get(i);
      numbers.remove(numbers.indexOf(number));
    }
    boolean first = true;
    if (numbers.isEmpty()) {
      System.out.println(0);
      return;
    }
    for (int i = 0; i < numbers.size(); i++) {
      System.out.print(first ? "" : " ");
      first = false;
      System.out.print(numbers.get(i));
    }
  }
}