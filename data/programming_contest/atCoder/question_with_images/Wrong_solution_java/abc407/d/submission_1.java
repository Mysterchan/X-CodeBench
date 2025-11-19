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
        int tt = 1;
        while (tt-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            long a[][] = new long[n][m];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < m; j++) {
                    a[i][j] = Long.parseLong(st.nextToken());
                }
            }
            long best = 0;

            for (int k = 0; k <= (1 << (n * m)); k++) {

                long xor = 0;
                boolean vis[][] = new boolean[n][m];

                boolean found = true;
                for (int i = 0; i < n && found; i++) {
                    for (int j = 0; j < m; j++) {
                        if (((k >> ((i * m) + j)) & 1) == 1) {

                            if (vis[i][j])
                                continue;
                            vis[i][j] = true;
                            if (i < n - 1 && (((k >> (((i + 1) * m) + j)) & 1) == 1) && !vis[i + 1][j]) {
                                vis[i + 1][j] = true;
                                continue;
                            }

                            if (j < m - 1 && (((k >> ((i * m) + j + 1)) & 1) == 1) && !vis[i][j + 1]) {

                                vis[i][j + 1] = true;
                                continue;
                            }

                            found = false;
                            break;
                        } else
                            xor = xor ^ a[i][j];
                    }
                }

                if (!found)
                    continue;
                best = Math.max(best, xor);

            }

            pw.println(solve(0, 0, a,new boolean[n][m]));
        }
        pw.flush();
    }

    public static long solve(int i, int j, long a[][], boolean vis[][]) {

        int n = a.length;
        int m = a[0].length;
        if (i >= n ) {
            return 0;
        }
        if (vis[i][j]) {
            if (j == m - 1) {
                return solve(i + 1, 0, a, vis);

            } else
                return solve(i, j + 1, a, vis);
        }

        else {

            long ans1 = a[i][j];
            if (j == m - 1) {
                ans1 ^= solve(i + 1, 0, a, vis);

            } else
                ans1 ^= solve(i, j + 1, a, vis);

            long ans2 = 0;
            if (i < n - 1) {

                if (!vis[i + 1][j]) {

                    vis[i][j] = true;
                    vis[i + 1][j] = true;

                    if (j == m - 1) {
                        ans2 ^= solve(i + 1, 0, a, vis);

                    } else
                        ans2 ^= solve(i, j + 1, a, vis);

                    vis[i][j] = false;
                    vis[i+1][j] = false;
                }

            }

            long ans3 = 0;

            if(j < m -1 ){
                if(!vis[i][j+1]){
                    vis[i][j] = true;
                    vis[i][j+1] = true;
                    ans3 ^= solve(i,j+1,a,vis);
                    vis[i][j] = false;
                    vis[i][j+1] = false;
                }
            }

            return Math.max(ans1,Math.max(ans2,ans3));

        }

    }
}