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
            char s[][] = new char[n][n];
            for (int i = 0; i < n; i++) {
                s[i] = br.readLine().toCharArray();
            }
            char t[][] = new char[n][n];
            for (int i = 0; i < n; i++) {
                t[i] = br.readLine().toCharArray();
            }

            int ans= n*n;

            ans = Math.min(ans,diff(s, t, n));
            s = helper(n,s);
            ans = Math.min(ans,diff(s, t, n)+1);
            s = helper(n, s);
            ans = Math.min(ans,diff(s, t, n)+2);
            s = helper(n, s);
            ans = Math.min(ans,diff(s, t, n)+3);
            pw.println(ans);

        }
        pw.flush();
    }

    public static int diff(char strans[][],char t[][],int n) {
        int count2 = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (strans[i][j] != t[i][j]) {
                    count2++;
                }

            }
        }
        return count2;
    }

    public  static char[][] helper(int n, char[][] s) {
        char strans[][] = new char[n][n];
        for (int i = 0; i < n; i++) {

            for (int j = 0; j < n; j++) {
                strans[i][j] = s[j][i];

            }
        }
        for (int i = 0; i < n; i++) {
            int k = 0;
            int l = n - 1;
            while (k < l) {
                char temp = strans[i][k];
                strans[i][k] = strans[i][l];
                strans[i][l] = temp;
                k++;
                l--;
            }
        }

        return strans;
    }
}