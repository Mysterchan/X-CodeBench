import java.util.*;
import java.io.*;

public class Main {
    static long mod = (int) 1e9 + 7;

    public static long pow(long a, long b) {
        long re = 1;
        while (b > 0) {
            if ((b & 1) == 1) {
                re = (re * a) % mod;
            }
            a = (a * a) % mod;
            b >>= 1;
        }
        return re;
    }

    public static void revArr(int[] arr) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }

    public static void sort(int[] a) {
        mergeSort(a, 0, a.length - 1);
    }

    private static void mergeSort(int[] arr, int left, int right) {
        if (left >= right)
            return;
        int mid = (left + right) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }

    private static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1, n2 = right - mid;
        int[] L = new int[n1], R = new int[n2];
        for (int i = 0; i < n1; i++)
            L[i] = arr[left + i];
        for (int i = 0; i < n2; i++)
            R[i] = arr[mid + 1 + i];
        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j])
                arr[k++] = L[i++];
            else
                arr[k++] = R[j++];
        }
        while (i < n1)
            arr[k++] = L[i++];
        while (j < n2)
            arr[k++] = R[j++];
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        int tt = Integer.parseInt(br.readLine());
        while (tt-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            char grid[][] = new char[n][m];
            for (int i = 0; i < n; i++) {
                grid[i] = br.readLine().toCharArray();
            }

            int re = 0;
            int dp[] = new int[n + 1];
            Arrays.fill(dp,50500);
            dp[0] = 0;

            for (int i = 0; i < n; i++) {

                if (i - 1 >= 0) {
                    char temp1[][] = new char[2][m];
                    for (int j = i - 1; j < i + 1; j++) {
                        for (int k = 0; k < m; k++) {
                            temp1[j - i + 1][k] = grid[j][k];
                        }
                    }

                    dp[i + 1] = Math.min(dp[i+1],dp[i - 1] + min(0, 0, temp1));
                }

                if (i < n - 1) {
                    char temp[][] = new char[2][m];
                    for (int j = i; j < i + 2; j++) {
                        for (int k = 0; k < m; k++) {
                            temp[j - i ][k] = grid[j][k];
                        }
                    }

                    dp[i + 1] = Math.min(dp[i+1],dp[i] + min(0, 0, temp));
                }

            }

            pw.println(dp[n]);
        }
        pw.flush();
    }

    public static int min(int i, int j, char grid[][]) {

        if (i == 2) {
            for (int y = 0; y < grid[0].length - 1; y++) {
                if (helper(0, y, grid)) {
                    return 50000;

                }
            }
            return 0;
        }

        if (grid[i][j] == '.') {
            if (j == grid[0].length - 1) {
                return min(i + 1, 0, grid);
            } else
                return min(i, j + 1, grid);
        } else {

            grid[i][j] = '.';
            int ca = Integer.MAX_VALUE;
            if (j == grid[0].length - 1) {
                ca = Math.min(ca, min(i + 1, 0, grid) + 1);
            } else
                ca = Math.min(ca, min(i, j + 1, grid) + 1);
            grid[i][j] = '#';

            if (j == grid[0].length - 1) {
                ca = Math.min(ca, min(i + 1, 0, grid));
            } else
                ca = Math.min(ca, min(i, j + 1, grid));

            return ca;

        }
    }

    public static boolean helper(int i, int j, char grid[][]) {
        if (grid[i][j] == '.' || grid[i][j + 1] == '.' || grid[i + 1][j] == '.' || grid[i + 1][j + 1] == '.')
            return false;
        return true;
    }
}