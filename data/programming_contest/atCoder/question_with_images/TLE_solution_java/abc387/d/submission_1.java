import java.util.*;

class Main {

  static Scanner sc = new Scanner(System.in);

  public static void main(String[] args) {
    int H = ni();
    int W = ni();
    String[] grid = new String[H];
    int startX = -1, startY = -1;
    for (int i = 0; i < H; i++) {
      grid[i] = nn();
    }
    char[][] gridChar = new char[H][W];
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        gridChar[i][j] = grid[i].charAt(j);
        if (gridChar[i][j] == 'S') {
          startX = i;
          startY = j;
        }
      }
    }
    int ans = Integer.MAX_VALUE;
    ans = Math.min(dfs(startX, startY, gridChar, new boolean[H][W], H, W, 0, 0, ans), ans);
    ans = Math.min(dfs(startX, startY, gridChar, new boolean[H][W], H, W, 0, 1, ans), ans);

    System.out.println(ans == Integer.MAX_VALUE ? -1 : ans);

    sc.close();
  }

  static int dfs(int x, int y, char[][] grid, boolean[][] visited, int H, int W, int count,
      int beforeMove, int ans) {
    if (x < 0 || x >= H || y < 0 || y >= W || visited[x][y] || grid[x][y] == '#') {
      return ans;
    }
    if (grid[x][y] == 'G') {
      return Math.min(ans, count);
    }
    visited[x][y] = true;

    if (beforeMove == 1) {
      ans = Math.min(dfs(x - 1, y, grid, visited, H, W, count + 1, 0, ans), ans);
      ans = Math.min(dfs(x + 1, y, grid, visited, H, W, count + 1, 0, ans), ans);
    } else {
      ans = Math.min(dfs(x, y - 1, grid, visited, H, W, count + 1, 1, ans), ans);
      ans = Math.min(dfs(x, y + 1, grid, visited, H, W, count + 1, 1, ans), ans);
    }
    visited[x][y] = false;
    return ans;
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