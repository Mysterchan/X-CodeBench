import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int t = sc.nextInt();
    StringBuilder sb = new StringBuilder();
    for (int tc = 0; tc < t; ++tc) {
      int n = sc.nextInt();
      int[] x = new int[n];
      int[] y = new int[n];
      for (int i = 0; i < n; ++i) {
        x[i] = sc.nextInt();
        y[i] = sc.nextInt();
      }

      sb.append(solve(x, y)).append('\n');
    }

    System.out.print(sb);
    sc.close();
  }

  static long solve(int[] x, int[] y) {
    int n = x.length;

    if (n == 1) {
      return 1;
    }

    // Find min and max for x and y
    int minX = Integer.MAX_VALUE, maxX = Integer.MIN_VALUE;
    int minY = Integer.MAX_VALUE, maxY = Integer.MIN_VALUE;
    for (int i = 0; i < n; ++i) {
      if (x[i] < minX) minX = x[i];
      if (x[i] > maxX) maxX = x[i];
      if (y[i] < minY) minY = y[i];
      if (y[i] > maxY) maxY = y[i];
    }

    // Precompute min2X, max2X, min2Y, max2Y excluding each point efficiently
    // To do this, find the top two min and max values for x and y

    // For x
    int minX1 = Integer.MAX_VALUE, minX2 = Integer.MAX_VALUE;
    int maxX1 = Integer.MIN_VALUE, maxX2 = Integer.MIN_VALUE;
    // For y
    int minY1 = Integer.MAX_VALUE, minY2 = Integer.MAX_VALUE;
    int maxY1 = Integer.MIN_VALUE, maxY2 = Integer.MIN_VALUE;

    for (int i = 0; i < n; ++i) {
      int val = x[i];
      if (val < minX1) {
        minX2 = minX1;
        minX1 = val;
      } else if (val < minX2) {
        minX2 = val;
      }
      if (val > maxX1) {
        maxX2 = maxX1;
        maxX1 = val;
      } else if (val > maxX2) {
        maxX2 = val;
      }

      val = y[i];
      if (val < minY1) {
        minY2 = minY1;
        minY1 = val;
      } else if (val < minY2) {
        minY2 = val;
      }
      if (val > maxY1) {
        maxY2 = maxY1;
        maxY1 = val;
      } else if (val > maxY2) {
        maxY2 = val;
      }
    }

    long result = (long)(maxX - minX + 1) * (maxY - minY + 1);

    for (int i = 0; i < n; ++i) {
      int curX = x[i];
      int curY = y[i];

      int curMinX = (curX == minX1) ? minX2 : minX1;
      int curMaxX = (curX == maxX1) ? maxX2 : maxX1;
      int curMinY = (curY == minY1) ? minY2 : minY1;
      int curMaxY = (curY == maxY1) ? maxY2 : maxY1;

      long xSide = (long)curMaxX - curMinX + 1;
      long ySide = (long)curMaxY - curMinY + 1;
      long cost = xSide * ySide;

      // If cost == n-1, add min side length (as per problem statement)
      if (cost == n - 1) {
        cost += Math.min(xSide, ySide);
      }

      if (cost < result) {
        result = cost;
      }
    }

    return result;
  }
}