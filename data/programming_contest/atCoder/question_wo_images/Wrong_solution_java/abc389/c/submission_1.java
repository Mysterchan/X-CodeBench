import java.io.*;
import java.util.*;

class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int Q = Integer.parseInt(br.readLine());

    List<Integer> snakes = new ArrayList<>();
    List<Integer> heads = new ArrayList<>();
    int shift = 0;
    int gap = 0;

    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < Q; i++) {
      StringTokenizer query = new StringTokenizer(br.readLine());
      int cmd = Integer.parseInt(query.nextToken());
      switch (cmd) {
        case 1 -> {
          int l = Integer.parseInt(query.nextToken());
          if (snakes.isEmpty())
            heads.add(0);
          else
            heads.add(heads.get(snakes.size() - 1) + snakes.get(snakes.size() - 1));
          snakes.add(l);
        }
        case 2 -> {
          gap += snakes.get(shift);
          shift++;
        }
        case 3 -> {
          int k = Integer.parseInt(query.nextToken()) - 1 + shift;
          int result = heads.get(k) - gap;
          sb.append(result).append('\n');
        }
      }
    }
    System.out.println(sb.toString());
  }
}