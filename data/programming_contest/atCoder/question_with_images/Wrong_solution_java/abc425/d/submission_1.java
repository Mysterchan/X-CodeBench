import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter out = new PrintWriter(System.out);
		StringTokenizer st = new StringTokenizer(br.readLine());
		int row = Integer.parseInt(st.nextToken());
		int col = Integer.parseInt(st.nextToken());
		char[][] grid = new char[row][col];
		boolean[][] visited = new boolean[row][col];
		Point[] stack = new Point[row * col];
		int count = 0;
		int stacki = 0;
		for (int i = 0; i < row; i++) {
			String r = br.readLine();
			for (int j = 0; j < col; j++) {
				grid[i][j] = r.charAt(j);
				if (grid[i][j] == '#') {
					visited[i][j] = true;
					stack[stacki++] = new Point(i, j);
				}
			}
		}
		int expand = 0;
		while (expand != stacki) {
			Point p = stack[expand++];
			int x = p.x;
			int y = p.y;
			if (canBlack(p, grid)) {
				count++;
				grid[x][y] = '#';
				if (x != 0 && !visited[x - 1][y]) {
					visited[x - 1][y] = true;
					stack[stacki++] = new Point(x - 1, y);
				}
				if (y != 0 && !visited[x][y - 1]) {
					visited[x][y - 1] = true;
					stack[stacki++] = new Point(x, y - 1);
				}
				if (x != grid.length - 1 && !visited[x + 1][y]) {
					visited[x + 1][y] = true;
					stack[stacki++] = new Point(x + 1, y);
				}
				if (y != grid[0].length - 1 && !visited[x][y + 1]) {
					visited[x][y + 1] = true;
					stack[stacki++] = new Point(x, y + 1);
				}
			}
		}
		out.print(count);
		out.flush();
	}

	public static boolean canBlack(Point p, char[][] grid) {
		int x = p.x;
		int y = p.y;
		int count = 0;
		if (grid[x][y] == '#') {
			return true;
		}
		if (x != 0) {
			count += grid[x - 1][y] == '#' ? 1 : 0;
		}
		if (y != 0) {
			count += grid[x][y - 1] == '#' ? 1 : 0;
		}
		if (x != grid.length - 1) {
			count += grid[x + 1][y] == '#' ? 1 : 0;
		}
		if (y != grid[0].length - 1) {
			count += grid[x][y + 1] == '#' ? 1 : 0;
		}
		return count == 1;
	}

	public static class Point {
		int x;
		int y;

		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

}