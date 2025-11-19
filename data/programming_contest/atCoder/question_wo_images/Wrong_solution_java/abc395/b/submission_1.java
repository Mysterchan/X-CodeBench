import java.util.*;

public final class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    final int N = Integer.parseInt(sc.next());
    sc.close();
    final int SIZE = N * N;
    final int LAST = N - 1;
    StringBuilder sb = new StringBuilder();
    for(int i = 0; i < SIZE; i++){
      int col = i % N;
      int row = i / N;
      boolean flag = col == 0 || row == 0 || col == LAST || row == LAST || col * row == LAST;
      sb.append(flag ? '#' : '.');
      if(col == LAST) sb.append('\n');
    }
    System.out.println(sb);
  }
}